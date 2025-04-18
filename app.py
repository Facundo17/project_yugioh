import cv2
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf

cap = cv2.VideoCapture(0)

#print(tf.__version__)

model = load_model("./model/yugioh_model.keras", compile=False)

class_names = ["Monster", "Spell", "Trap"]  # Debe coincidir con las carpetas


while True:
    ret, frame = cap.read()
    # Aquí puedes hacer crop, redimensionar y preprocesar la imagen
    img = cv2.resize(frame, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # predicción
    label = 'testing'
    #prediction = model.predict(img)
    #label = np.argmax(prediction)

    # Mostrar la predicción
    cv2.putText(frame, f"Tipo de carta: {label}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Yu-Gi-Oh Classifier", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()