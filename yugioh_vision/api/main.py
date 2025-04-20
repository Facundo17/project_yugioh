import uuid
import redis
import json
import base64
import time
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Habilitar CORS
# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Podés restringir a ["http://localhost:8080"] si querés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# redis para comunicación con el modelo
db = redis.Redis(host="redis", port=6379, db=0)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_data = await file.read()
    encoded = base64.b64encode(image_data).decode("utf-8")
    task_id = str(uuid.uuid4())

    payload = {
        "id": task_id,
        "image": encoded
    }

    # Enviar tarea
    db.rpush("tasks", json.dumps(payload))

    # Esperar respuesta
    for _ in range(30):
        if db.exists(task_id):
            result = json.loads(db.get(task_id))
            db.delete(task_id)
            return JSONResponse(content=result)
        time.sleep(1)

    return JSONResponse(content={"error": "Timeout"}, status_code=504)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)