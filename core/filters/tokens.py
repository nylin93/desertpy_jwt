from flask import request, current_app, Response
from functools import wraps
from jose.jwt import decode
from jose.exceptions import JWTError
import time


def require_auth(func):
	@wraps(func)
	def check_jwt(*args, **kwargs):
		# TODO: 1. Check the JWT exists in request.cookies
		# TODO: 2 .Try to decode the JWT
		# TODO: 3. Check the expiration date of the JWT 
		return func(*args, **kwargs)

	return check_jwt
