from fastapi import FastAPI

from rabbitmqProducer import publish


app= FastAPI()

@app.get("/publish")
def publishMessage(data):
    publish(data)
    return({'message': 'published message'})