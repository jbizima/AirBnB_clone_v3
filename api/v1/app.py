#!/usr/bin/python3
"""First api with flask and python"""

import os
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={"/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False  # allow /api/v1/states/ and /api/v1/states

host = os.getenv("HBNB_API_HOST", "0.0.0.0")
port = os.getenv("HBNB_API_PORT", 5000)


@app.errorhandler(404)
def error_not_found(self):
    """404 error but return empty dict"""
    return make_response(jsonify({"error": "Not found"}), 404)


@app.teardown_appcontext
def teardown(*args, **kwargs):
    """close storage"""
    storage.close()


if __name__ == "__main__":
    """Flask Boring App"""
    # print(app.url_map)
    app.run(host=host, port=port)
