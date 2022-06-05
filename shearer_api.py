from fastapi import FastAPI
import json
from datetime import datetime

app = FastAPI()

@app.get("/shearerpos")
async def shearerpos():
	f = open('shearer_storage.json')
	data = json.load(f)
	f.close()
	return data