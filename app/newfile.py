import os

from flask import Flask 

port = int(os.environ['PORT'])
app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello World Cup!</h1><br><h2>感動をありがとう！！</h2>'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=81)
  