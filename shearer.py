import sys
import requests
import datetime
import time
import random

now = datetime.datetime.now()

URL = "http://localhost:4000/shearerpos"
headers = {
  'Content-Type': 'application/json'
}

reverse = False
currentPosition = 0

def getTimeAndPosition():
	global reverse, currentPosition
	change = random.randint(1,10)
	if (reverse):
		if currentPosition - change < 0:
			currentPosition = 0
			reverse = False
		else:
			currentPosition = currentPosition - change
	else:
		if currentPosition + change > 100:
			currentPosition = 100
			reverse = True
		else:
			currentPosition = currentPosition + change

	return {"time": str(now), "position": currentPosition}

def main():
	while True:
		data = getTimeAndPosition()
		print(data)
		r = requests.post(url = URL, headers = headers, json = data)
		# extracting response text 
		print("Res: ", r.status_code)
		time.sleep(5)

if __name__ == "__main__":
	currentPosition = int(sys.argv[1])
	reverse = bool(sys.argv[2])
	main()