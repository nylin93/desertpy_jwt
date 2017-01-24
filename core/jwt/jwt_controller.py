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
	now = time.time()
	token = {
		'iss': now,
		'exp': now + jwt.expiration
	}

	cookie = encode(token, jwt.secret, algorithm='HS256')
	res = Response(
		response=json_util.dumps({'authenticated': True}),
		status=200,
		mimetype='application/json'
	)

	res.set_cookie(jwt.name, cookie, 
		expires=now+jwt.expiration, 
		httponly=True
	)
	return res
