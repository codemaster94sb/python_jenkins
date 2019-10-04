#!/usr/bin/env python
from flask import Flask, request, Response
app = Flask(__name__)


@app.route('/math/<number1>/<operation>/<number2>', methods=['GET'])
def math(number1, operation, number2):
    try:
        if request.method == 'GET':
            if not isinstance(int(number1), int):
                raise Exception('Please enter a valid number on position :number1:')
            if not isinstance(int(number2), int):
                raise Exception('Please enter a valid number on position :number2:')
            if not isinstance(operation, str):
                raise Exception('Please use a valid operation on position :operation:')
            result = None
            if operation == '+':
                result = int(number1)+int(number2)
            elif operation == '-':
                result = int(number1)-int(number2)
            elif operation == '/':
                result = int(number1)/int(number2)
            elif operation == '*':
                result = int(number1)*int(number2)
            else:
                raise Exception('This operation is not yet supported.')
            json_response = {'result' : result}
            response = Response()
            response.data = str(json_response)
            response._status_code = 200
            return response
        else:
            raise Exception('Please do a POST request.')
    except Exception as e:
        response = {'error': str(e)}
        return response.__str__()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
