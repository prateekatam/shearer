from fastapi import FastAPI
import json
from datetime import datetime

app = FastAPI()

def statusCheck(timestamp):
	timestamp = datetime.strptime(timestamp,"%Y-%m-%d %H:%M:%S.%f")
	now = datetime.now()
	diff = (now-timestamp).seconds
	if (diff > 10):
		return "ERROR"
	return "OK"

@app.get("/shearerpos")
async def shearerpos():
	f = open('data.json')
	data = json.load(f)
	data['status'] = statusCheck(data['time'])
	f.close()
	return data