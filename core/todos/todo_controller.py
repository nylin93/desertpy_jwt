from flask import request, Response, Blueprint
from bson import json_util
from bson.objectid import ObjectId

from core.filters import require_auth


todos = Blueprint('todos', __name__)
todos.db = None

@todos.record
def todos_config(setup_state):
	todos.db = setup_state.app.config['MONGODB'].todos

@todos.route('/todos', methods=['GET'], strict_slashes=False)
@require_auth
def get_todos():
	records = list(todos.db.find().sort('updated_at', -1))

	return Response(
		response=json_util.dumps(records),
		status=200,
		mimetype='application/json'
	)

@todos.route('/todos', methods=['POST'], strict_slashes=False)
@require_auth
def create_todo():
	body = request.get_json()

	todo = {
		'title': body['title'],
		'description': body['description']
	}

	todos.db.insert(todo)
	return Response(
		response=json_util.dumps(todo),
		status=201,
		mimetype='application/json'
	)

@todos.route('/todos/<string:todo_id>', methods=['PUT'], strict_slashes=False)
@require_auth
def update_todo(todo_id):
	body = request.get_json()

	updated_todo = {
		'title': body['title'],
		'description': body['description']
	}

	todos.db.replace_one({'_id': ObjectId(todo_id)}, updated_todo)
	return Response(
		response=json_util.dumps(updated_todo),
		status=200,
		mimetype='application/json'
	)

@todos.route('/todos/<string:todo_id>', methods=['DELETE'], strict_slashes=False)
@require_auth
def delete_todo(todo_id):
	todos.db.delete_one({'_id': ObjectId(todo_id)})

	return Response(status=204)
