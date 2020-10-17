import flask
import json
from flask import request, make_response
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

headers = {"Content-Type": "application/json"}

@app.route('/total', methods=['GET'])
def home():
    #first try to get the numbers from the values property
    numbers_to_add = request.values.getlist("n", type=float)
    
    if len(numbers_to_add) == 0: 
        #when nothing available in values, check data property
        #but first make sure that the size of data is not too big 
        #or it might cause memory problems on the server
        if request.content_length < 100*1024*1024:  
            data = request.data
            try:
                numbers_to_add = json.loads(data).get("n")
            except Exception as exc: 
                #when param N not found, raise the exception
                raise Exception('Argument "n" is not found') from exc
        else:
          raise Exception("Content is too big")

    #if no numbers to add found, raise the exception
    if numbers_to_add is None :
        raise Exception('Argument "n" is not found')
    
    #calculate the total
    total = {'total' : sum(numbers_to_add)}
    
    #return the result
    return make_response(total, 200)

if __name__ == '__main__':
    app.run()
