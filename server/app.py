#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = "\n".join(str(i) for i in range(parameter))
    return Response(numbers, mimetype='text/plain')

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return 'Invalid numbers provided', 400

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Division by zero is not allowed', 400
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return 'Division by zero is not allowed', 400
        result = num1 % num2
    else:
        return 'Invalid operation provided', 400
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
