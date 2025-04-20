from PIL import Image
from io import BytesIO
import numpy as np
import redis
import time
import json
from tensorflow.keras.models import load_model

# ejecutar el message broker
db = redis.Redis(host='redis', port=6379, db=0)

# cargar el modelo
model = load_model("yugioh_model.h5")

# Cantidad de clases para esta demo
class_names = ["Monster", "Spell", "Trap"]

def predict(img) -> np.ndarray:
    """
    return: np.ndarray bidimensional (1, num_classes), con las probabilidades de cada clase
    1 es el número de imágenes (batch_size)
    num_classes es la cantidad de clases (En este caso son 3: Monster, Spell, Trap)
    """    
    prediction = model.predict(img)
    
    return prediction

def read_imagefile(file) -> np.ndarray:
    image = Image.open(BytesIO(file)).convert("RGB")
    image = image.resize((128, 128))
    img_array = np.asarray(image) / 255.0
    return np.expand_dims(img_array, axis=0)


# Utilizando redi como message broker

# funcion de prueba
def classify_process():
    """
    Loop indefinitely asking Redis for new jobs.
    When a new job arrives, takes it from the Redis queue, uses the loaded ML
    model to get predictions and stores the results back in Redis using
    the original job ID so other services can see it was processed and access
    the results.

    Load image from the corresponding folder based on the image name
    received, then, run our ML model to get predictions.
    """
    
    while True:
        # Take a new job from Redis
        q = db.brpop("service_yugioh_queue")[1]
        
        # Decode the JSON data for the given job
        q = json.loads(q.decode("utf-8"))
        
        # Important! Get and keep the original job ID
        job_id = q["id"]
        
        # Run the loaded ml model (use the predict() function)
        class_name, pred_probability = predict(
            q["image_name"]
        )
        
        # Prepare a new JSON with the results
        output = {"prediction": class_name, "score": pred_probability}

        # Store the job results on Redis using the original
        # job ID as the key
        # Store the job results on Redis using the original job ID as the key
        db.set(job_id, json.dumps(output))

        # Sleep for a bit
        time.sleep(0.05)




if __name__ == "__main__":
    # Now launch process
    print("Ejecutando Servicio ML...")
    classify_process()