from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/1_second")
async def endpoint1():
    # time.sleep(1)  # Wait for 1 seconds
    i = 0
    for _ in range(10000):
        i = _
    return {"message": "Response after 1 seconds"}

@app.get("/endpoint1")
async def endpoint1():
    time.sleep(2)  # Wait for 2 seconds
    return {"message": "Response after 2 seconds"}

@app.get("/endpoint2")
async def endpoint2():
    time.sleep(5)  # Wait for 5 seconds
    return {"message": "Response after 5 seconds"}

@app.get("/endpoint3")
async def endpoint2():
    time.sleep(10)  # Wait for 10 seconds
    return {"message": "Response after 10 seconds"}

@app.get("/endpoint4")
async def endpoint3():
    time.sleep(20)  # Wait for 20 seconds
    return {"message": "Response after 20 seconds"}
