import os
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    return "My Second Image"

@app.route("/container")
def container():
    return "pythion2 run succesfully"

if __name__ == "__main__":
    print("2nd Image")
    app.run()