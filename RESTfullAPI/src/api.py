import flask
from flask import request, make_response
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

headers = {"Content-Type": "application/json"}

def get_total(list_of_numbers):
 return sum(list_of_numbers)

def get_total_in_json(total):
 return {'total' : total}

@app.route('/total', methods=['GET'])
def home():
 numbers_to_add = request.values.getlist("n", type=int)

 total = get_total(numbers_to_add)

 data = get_total_in_json(total)

 return make_response(json.dumps(data), 200, headers)

if __name__ == '__main__':
    app.run()
