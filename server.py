import sys, os

BASE_DIR = os.path.join(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
	sys.path.append(BASE_DIR)

from core import create_app
app = create_app('config.DevConfig')

app.run(port=5000, debug=True, threaded=True)
