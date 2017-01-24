from pymongo import MongoClient


class DevConfig():
	JWT_SECRET = '0f86f3a22a57c624bf3b31d9ebe803ca'
	JWT_EXPIRATION = 259200
	JWT_NAME = 'desertpy'
	MONGODB = MongoClient().desertpy
	HEADER_KEY = 'X-REQUESTED-WITH'
	HEADER_VALUE = 'DESERTPY-MEETUP'
