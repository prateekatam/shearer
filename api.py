from fastapi import FastAPI
import json
from datetime import datetime

app = FastAPI()

# check if the shearer is working by comparing it's last emit. If last emit more than 10 seconds, then error.
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
	status = statusCheck(data['time'])
	if status == "ERROR":
		data['position'] = None
	data['status'] = status
	f.close()
	return data