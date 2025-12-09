from flask import Flask
import uuid

app = Flask(__name__)

@app.route('/')
def index():
  return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flask Basic</title>
</head>
<body>
  <h1> Home Page </h1>
    <hr>
  
</body>
</html>
"""


@app.route('/name')
def name():
  return f'<h1>Alexter</h1>'

@app.route('/user/<username>')
def user(username):
  return f'<h1>My name is {username}</h1>'

@app.route('/calculatoe/addition/<int:A>/<int:B>')
def addition(A, B):
  result = A + B
  return f'<h1>{A} + {B} = {A+B}</h1>'

@app.route('/calculatoe/subtraction/<int:A>/<int:B>')
def subtraction(A, B):
  result = A - B
  return f'<h1>{A} - {B} = {A-B}</h1>'

@app.route('/calculatoe/multiply/<int:A>/<int:B>')
def multiply(A, B):
  result = A * B
  return f'<h1>{A} * {B} = {result}</h1>'

@app.route('/calculatoe/divide/<int:A>/<int:B>')
def divide(A, B):
  result = A / B
  return f'<h1>{A} / {B} = {result}</h1>'

@app.route('/secretkey/<uuid:sk>')
def my_secret_key(sk):
  return f'<h1>My Secret Key: {sk}</h1>'

#if __name__ == '__main__':
#  app.run(debug=True)