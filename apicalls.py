from authorization import *
from urls import *
def status(auth):
	arg = "/1.1/statuses/lookup.json"
	ARG_URL = API_URL + arg
	response = requests.get(ARG_URL,auth=auth)
	print json.dumps(response.json(), indent =4)
	return arg
	
	
def  myretweets(auth):
	arg = "/1.1/statuses/retweets_of_me.json"
	ARG_URL = API_URL + arg
	response = requests.get(ARG_URL,auth=auth)
	print json.dumps(response.json(), indent =4)
	return arg

def followers(auth):
	arg = "/1.1/followers/list.json"
	ARG_URL = API_URL + arg
	response = requests.get(ARG_URL,auth=auth)
	print json.dumps(response.json(), indent =4)
	return arg
	
def favorites(auth):
	arg = "/1.1/favorites/list.json"
	ARG_URL = API_URL + arg
	response = requests.get(ARG_URL,auth=auth)
	print json.dumps(response.json(), indent =4)
	return arg