from flask import current_app, request, Response
from bson import json_util


def require_from_header():
	header_key = current_app.config['HEADER_KEY']
	header_val = current_app.config['HEADER_VALUE']

	if header_key not in request.headers:
		return Response(
			response=json_util.dumps({'error': 'Missing header key'}),
			status=401,
			mimetype='application/json'
		)
	elif header_val != request.headers[header_key]:
		return Response(
			response=json_util.dumps({'error': 'Unrecognized request entity'}),
			status=401,
			mimetype='application/json'
		)
