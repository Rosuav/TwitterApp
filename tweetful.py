import authorization
import json
import requests
import sys
import argparse
import gettwitter
import logging
from apicalls import *
from urls import *
logging.basicConfig(filename="tweetoutput.log", level=logging.DEBUG)
	
def make_parser():
	logging.info ("Constructing parser")
	parser = argparse.ArgumentParser(description="Interact with twitter api")
	parser.add_argument("get", help ="GET requests to twitter")
	return parser
	
def main():
	logging.info("Starting tweetful")
	parser = make_parser()
	arguments = parser.parse_args(sys.argv[1:])
	arguments = vars(arguments)
	auth = authorization.authorize()
	
	if arguments['get']=='status':
		status(auth)
		
	elif  arguments['get']=='myretweets':
		myretweets(auth)
	
	elif  arguments['get']=='followers':
		followers(auth)
	
	elif  arguments['get']=='favorites':
		favorites(auth)
		

if __name__ == "__main__":
	main()
		
	
	