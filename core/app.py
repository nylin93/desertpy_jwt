from flask import Flask

from .filters import require_from_header


def create_app(config):
	app = Flask(__name__)
	app.config.from_object(config)

	configure_blueprints(app)
	configure_hooks(app)

	return app

def configure_blueprints(app):
	from .todos import todos
	from .jwt import jwt

	app.register_blueprint(todos, url_prefix='/api')
	app.register_blueprint(jwt, url_prefix='/api')

def configure_hooks(app):
	app.before_request(require_from_header)
