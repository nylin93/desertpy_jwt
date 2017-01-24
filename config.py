from pymongo import MongoClient


class DevConfig():
	JWT_SECRET = 'd910aeb2a36e2f082e2b0c6aa5b93ee263262362f37fb98cd90b959fbc26706c'
	MONGODB = MongoClient().desertpy
