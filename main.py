from flask import Flask

app = Flask(__name__)
@app.routes("/")
def home():
	return "<h1>Nginx & Gunicorn</h1>"
