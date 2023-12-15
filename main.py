#The route accepts a POST request with JSON data in the format {"number": x} where
#x is an integer. The route should return a JSON o
#bject {"result": y}, where y is the square o
#f x. If the request is not a POST request,
#the route should return a 405 status code. If the request does not contain JSON d
#ata or the JSON data does not contain the key "number", or the value of
#"number" is not an integer, the route should return a 400 status code with th
 #   e message "Bad Request"


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate_square():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            if 'number' in data and isinstance(data['number'], int):
                number = data['number']
                result = number ** 2
                return jsonify({'result': result})
            else:
                return jsonify({'message': 'Bad Request'}), 400
        else:
            return jsonify({'message': 'Bad Request'}), 400
    else:
        return jsonify({'message': 'Method Not Allowed'}), 405

    if __name__=='__main__':
        app.run()
