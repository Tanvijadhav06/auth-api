from fastapi import FastAPI

app = FastAPI(title="User Authentication API")


@app.get("/")
def root():
    return {"message": "Authentication API is running"}
