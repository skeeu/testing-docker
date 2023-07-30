from fastapi import FastAPI

app = FastAPI()
subapi = FastAPI()
app.mount("/api", subapi)


@subapi.get("/")
async def index():
    return {"message": "Hello World"}


@subapi.get("/hello")
async def hello():
    return {"message": "Hello World"}


@subapi.get("/lol")
async def heo():
    return {"message": "lol"}
