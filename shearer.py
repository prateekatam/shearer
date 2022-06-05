import sys
import os
import requests
import datetime
import time
import random
import json

# URL = "http://localhost:4000/shearerpos"
# headers = {
#   'Content-Type': 'application/json'
# }

reverse = False
currentPosition = 1

def where_json(file_name):
    return os.path.exists(file_name)

def getTimeAndPosition():
	global reverse, currentPosition
	now = datetime.datetime.now()
	change = random.randint(1,10)
	if (reverse):
		if currentPosition - change < 1:
			currentPosition = 1
			reverse = False
		else:
			currentPosition = currentPosition - change
	else:
		if currentPosition + change > 100:
			currentPosition = 100
			reverse = True
		else:
			currentPosition = currentPosition + change

	# Emit. Nomally, write to a DB here. 
	with open("shearer_storage.json", "w") as i :
		json.dump({"time": str(now), "position": currentPosition}, i)

	return {"time": str(now), "position": currentPosition}

def main():
	if where_json('shearer_storage.json'):
		pass
	else:
		with open('shearer_storage.json', 'w') as outfile:  
				json.dump({}, outfile)	
	
	while True:
		data = getTimeAndPosition()
		print(data)
		# r = requests.post(url = URL, headers = headers, json = data)
		# print("Res: ", r.status_code)
		time.sleep(5)

if __name__ == "__main__":
	currentPosition = int(sys.argv[1])
	reverse = bool(sys.argv[2])
	main()