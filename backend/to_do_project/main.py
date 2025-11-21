from fastapi import FastAPI

app = FastAPI(
    title="To-Do List API",
    description="API con Arquitectura Limpia",
    version="1.0.0"
)

@app.get("/", summary="Health endpoint")
def status_check():
    return {"message":"200 ok"}