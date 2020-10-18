SOFTWARE ENGINEER PYTHON TEST
=============================

Create a REST endpoint that return the sum of a list of numbers e.g. [1,2,3] => 1+2+3 = 6 You are free to use any Python 3 framework,
however, try and keep the usage of the third- party library to a minimum.
The list of numbers is expected to arrive from a backend service and for this test you can hard code the list using the following line.
```python
numbers_to_add = list(range(10000001))
```
The URL of the endpoint and the sample response is as follows:
Request: `http://localhost:5000/total`
Response:
```json
{
"total": 6
}
```
Please provide the source code, tests, documentations and any assumptions you have made.
Note: We are looking for the candidate’s “Software Engineering” ability not just the Python programming skills.

Assumptions
-----------
1) The input argument for the API coming from the backend should be in a JSON format {key/value} therefore I suggest using parameter `n` as the key value:
```python
{n:[1,2,3]}
```
2) The amount of the input data should be limited to 100Mb or it might cause memory problems on the server. I suggest throwing an exception in case if the backend submit larger data   


Installation
------------

You can checkout and install the source from the [github repository](https://github.com/directlinegroup/python_test):

    git clone https://github.com/directlinegroup/python_test.git
    cd python_test
    pip install -r requirements.txt


Execution
---------

To run the server locally execute the following command in the folder where python_test was installed:

```
python3 src/api.py 
```

You should immediately see the confirmation that the server is up and running:

```
* Serving Flask app "api" (lazy loading)
 * Environment: production
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
```

Tests
---------

To run the unit tests open the folder `python_test/tests` in another terminal window and execute the following:

```
python3 -m unittest discover -v
```

You should get the following response

```
test_sum (test_api.TestDumps) ... ok
test_sum (test_api.TestFloat) ... ok
test_sum (test_api.TestJSON) ... ok
test_sum (test_api.TestMillion) ... ok
test_sum (test_api.TestParam) ... ok
test_sum (test_api.TestRandomMillion) ... ok
test_sum (test_api.TestString) ... ok
test_sum (test_api.TestSum) ... ok
test_sum (test_api.TestWrongParam) ... ok
test_sum (test_api.TestWrongParamDumps) ... ok

----------------------------------------------------------------------
Ran 10 tests in 38.092s

OK
```

Total API
---------
The API supports the GET and POST methods and returns the total of the given numbers e.g. `[1,2,3] => 1+2+3 = 6`

To sum up the list of numbers, you should send them as array with `n` as a key e.g. `{n:[1,2,3]}` to the end point `http://localhost:5000/total`

The response you receive would be in the JSON format:
```json
{
"total": 6
}
```

If you were constructing the URL by hand, this data would be given as key/value pairs in the URL after a question mark, e.g. `http://localhost:5000/total?n=1&n=2&n=3`

Or you can use any available third party frameworks to access the Total API but the following example is written in Python using [Requests]( https://requests.readthedocs.io/en/master/):

```python
import requests   
 
url = 'http://localhost:5000/total'
numbers_to_add = {n:[1,2,3]}

response = requests.get(url, data= numbers_to_add)

print(response.text)

# {
# "total": 6
# }

```

You may want to send data that is not form-encoded. If you pass it in a string instead of a dict, that data will be posted directly. The Total API accepts JSON-Encoded POST/PATCH data:

```python
import json

url = 'http://localhost:5000/total'
numbers_to_add = {n:[1,2,3]}

response = requests.get(url, data= json.dumps(numbers_to_add))
```

Exceptions
----------
If you try to access the API without sending the list or not using the parameter `n` in the requests, you will receive the following error:

```
Argument "n" is not found
```

If you submit a large amount of data (over 100Mb), the Total API will raise another error:

```
Content is too big
```


