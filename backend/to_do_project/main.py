from fastapi import FastAPI

app = FastAPI()

@app.get("/", summary="Health endpoint")
def status_check():
    return {"message":"200 ok"}