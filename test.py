from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def aid_web():
    return "Hello Aid!"


#C:\Z_Ddrive\aid_web\aid.html

#python3 -m uvicorn main:app --reload