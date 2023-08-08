# app/routes.py
from flask import jsonify

from app import app

@app.route('/api/v1/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello, World!'), 200
