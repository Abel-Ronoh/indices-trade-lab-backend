# app/__init__.py
from flask import Flask

app = Flask(__name__)

# Import routes defined in routes.py
from app import routes
