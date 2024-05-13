from flask import Flask, jsonify, request
from flask_cors import CORS
import script
import connector
from instagrapi import Client

app = Flask(__name__)
cors = CORS(app)
app.debug = True


@app.route("/")
def test():
    return "hello world"

@app.route("/api")
def hello_world():
    print("running")
    api = Client()
    database     = connector.connect()
    print("logged in")
    api.login('Automagic_Memes','Qwerty@12345')
    script.main(api,database)
    return "done"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0",port=3143)