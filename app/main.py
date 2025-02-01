from fastapi import FastAPI
from routers import task
from routers import user


app = FastAPI()

app.include_router(task.router)
app.include_router(user.router)

@app.get('/')
async def answer():
    return {"message": "Welcome to Taskmanager"}
