from flask import Flask
from activity.routes import configure

app = Flask(__name__)
configure(app)
