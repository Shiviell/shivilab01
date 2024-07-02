from flask import Flask, request, jsonify
import os
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify("Hello, Flask!")

@app.route("/env")
def environ():
    return jsonify(str(os.environ))

@app.route("/env/<path>")
def path(path):
    return jsonify(os.environ.get(path))

@app.route("/dir")
def dir():
    return jsonify(os.listdir(os.getcwd()))

@app.route("/dir/<name>")
def filename(name):
    try:
        f = open(name,'r')
        content = f.read()
    except:
        content = "problem with file name"
    return jsonify(content)

if __name__ == '__main__':
    app.run(debug=True)