import redis
import json
import base64
import time
import io
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Conectar a Redis
db = redis.Redis(host='redis', port=6379, db=0)
model = load_model("yugioh_model.h5")
class_names = ["Monster", "Spell", "Trap"]

print("🔁 Esperando tareas...")

while True:
    task = db.blpop("tasks")
    if task:
        _, data = task
        payload = json.loads(data)
        task_id = payload["id"]
        image_data = base64.b64decode(payload["image"])

        # Preprocesar imagen
        image = Image.open(io.BytesIO(image_data)).convert("RGB").resize((128, 128))
        image = np.array(image) / 255.0
        image = np.expand_dims(image, axis=0)

        prediction = model.predict(image)[0]
        predicted_label = class_names[np.argmax(prediction)]

        # Guardar resultado
        result = {
            "label": predicted_label,
            "confidence": float(np.max(prediction))
        }
        db.set(task_id, json.dumps(result))
