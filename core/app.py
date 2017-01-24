from flask import Flask


def create_app(config):
	app = Flask(__name__)
	app.config.from_object(config)

	configure_blueprints(app)

	return app

def configure_blueprints(app):
	from .todos import todos

	app.register_blueprint(todos, url_prefix='/api')
