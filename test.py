from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def aid_web():
    return "Hello Aid!"


#python3 -m pipenv run

#python3 -m uvicorn test:app --reload