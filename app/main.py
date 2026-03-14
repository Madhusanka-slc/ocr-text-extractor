from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home_view():
    return {"message": "FastAPI is running.."}


@app.post("/")
def home_detail_view():
    return {"message": "FastAPI is running.."}