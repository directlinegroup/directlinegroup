import flask
import json
from flask import request, make_response
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

headers = {"Content-Type": "application/json"}

@app.route('/total', methods=['GET'])
def home():
    print(datetime.now(tz=None), "API started")
    numbers_to_add = request.values.getlist("n", type=float)
    print(datetime.now(tz=None), len(numbers_to_add), "numbers_to_add:", numbers_to_add[0:100])
    if len(numbers_to_add) == 0:
        if request.content_length < 1024**3:
            data = request.data
            #print(datetime.now(tz=None), "data:", data)
            #if data is not None:
            try:
                numbers_to_add = json.loads(data).get("n")
            except Exception as exc:
                raise Exception('Argument "n" is not found') from exc
        else:
          raise Exception("Content is too big")

    if numbers_to_add is None :
        raise Exception('Argument "n" is not found')
    
    total = {'total' : sum(numbers_to_add)}

    return make_response(total, 200)

if __name__ == '__main__':
    app.run()
