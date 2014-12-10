import authorization
import json
import requests
import sys
import argparse
import gettwitter
from urls import *
def main():
	
	parser = argparse.ArgumentParser(description='Interact with twitterAPI')
	parser.add_argument('-twitter', help='Add this switch to show your retweets. Options are status,myretweets,followers,favorites,hometimeline')
	args = parser.parse_args()
		
	for arg in sys.argv:
		if sys.argv[2] == "status":
			arg = "/1.1/statuses/lookup.json"
		elif sys.argv[2] == "myretweets":
			arg = "/1.1/statuses/retweets_of_me.json"
		elif sys.argv[2] == "followers":
			arg = "/1.1/followers/list.json"
		elif sys.argv[2] == "myretweets":
			arg = "/1.1/statuses/retweets_of_me.json"
		elif sys.argv[2] == "hometimeline":
			arg = "/1.1/statuses/home_timeline.json"
		elif sys.argv[2] == "favorites":
			arg = "/1.1/favorites/list.json"
		
	
	ARG_URL = API_URL + arg 
	print ARG_URL 
	auth = authorization.authorize()
	response = requests.get(ARG_URL,auth=auth)
	print json.dumps(response.json(), indent =4)

if __name__ == "__main__":
	main()