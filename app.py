from flask import Flask

app = Flask(__name__)

@app.route('/')

def start():
  return "200 OK!"

app.run(port=5000)