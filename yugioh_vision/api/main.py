from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Image Prediction API", version="0.0.1")

@app.get("/")
def read_root():
    return {"mensaje": "API funcionando"}

# esta es una forma en la que una vez levantado el servicio en docker, el API se ejecute.
# Aquí configuras el puerto
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

