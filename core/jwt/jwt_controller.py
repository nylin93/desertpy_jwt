from bson import json_util
from flask import request, Response, Blueprint
from jose.jwt import encode
import time


jwt = Blueprint('jwt', __name__)
jwt.secret, jwt.expiration, jwt.name = None, None, None

@jwt.record
def jwt_config(setup_state):
	jwt.secret = setup_state.app.config['JWT_SECRET']
	jwt.expiration = setup_state.app.config['JWT_EXPIRATION']
	jwt.name = setup_state.app.config['JWT_NAME']

@jwt.route('/jwt', methods=['POST'], strict_slashes=False)
def create_jwt():
	# Pretend to do some backend lookups to check password etc.
	# TODO Create a token and encode it
	# TODO then set the cookie in the response with httponly=True 

	pass
