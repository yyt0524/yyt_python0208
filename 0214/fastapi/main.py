# -*- coding: UTF-8 -*-
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def say_hello():
    return {'code':200, 'message':'hello fastapi'}