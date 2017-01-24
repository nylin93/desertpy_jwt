from bson import json_util
from flask import request, current_app, Response
from functools import wraps
from jose.jwt import decode
from jose.exceptions import JWTError
import time


def require_auth(func):
	@wraps(func)
	def check_jwt(*args, **kwargs):
		now = time.time()
		conf = current_app.config
		print(request.cookies)
		if conf['JWT_NAME'] not in request.cookies:
			return Response(
				response=json_util.dumps({'error 1': 'Unauthorized'}),
				status=401,
				mimetype='application/json'
			)
		cookie, token = request.cookies[conf['JWT_NAME']], None
		try:
			token = decode(cookie, conf['JWT_SECRET'], algorithms='HS256')	
		except JWTError:
			return Response(
				response=json_util.dumps({'error 2': 'Unauthorized'}),
				status=401,
				mimetype='application/json'
			)
			
		if now > token['exp']:
			return Response(
				response=json_util.dumps({'error 3': 'Unauthorized'}),
				status=401,
				mimetype='application/json'
			)

		return func(*args, **kwargs)

	return check_jwt
