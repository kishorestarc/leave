from app import app
from flask import Flask

@app.route('/')
def index():
	return 'hello hello'

