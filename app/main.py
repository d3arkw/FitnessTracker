from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {'message': 'The app is ready to use'}