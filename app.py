import os
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    return "My first Images"

@app.route("/container")
def container():
    return "Container run succesfully"

if __name__ == "__main__":
    app.run()