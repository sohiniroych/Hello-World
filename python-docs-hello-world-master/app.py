from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("Handling request to homepage!")
    return "Hello, to Azure!"
