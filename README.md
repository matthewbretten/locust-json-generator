# locust-json-generator

Locust project for generating json data
===========================

This suite is an example to dynamically generate large amounts of JSON documents and still utilising Locust to control different volumes of certain data.

Prerequisites
-------------

* Python3

Installing packages
---------------
```bash
pip3 install -r requirements.txt
```

Running mock api to test against
---------------
Run these commands in a separate window to leave the mock api running
Windows
```bash
SET flask_app=src/mock_api.py
flask run
```
Unix
```bash
export FLASK_APP=src/mock_api.py
flask run
```

Running load tests
---------------
```bash
locust -f locustfiles/example_load_test.py --headless -u 1 -r 1 -t 5s --host "http://localhost:5000"
```

Features
----------------
* Dynamic JSON document generation

Behaviour
---------------
When this code is run, it will attempt to perform POST HTTP requests to http://localhost:5000 (as I was running a local Python Flask application to test receiving the requests).
As part of the POST request, it will include the generated JSON as part of the request body.

Sample data
---------------
This code will generate JSON data that looks like this as part of each request:
```json
{
  "customer": {
    "name": "Sarah Brown",
    "age": 56,
    "countryCode": "GB"
  },
  "totalPrice": 500,
  "items": [
    {
      "basketItemId": 2,
      "description": "Television",
      "price": 500
    }
  ],
  "dateCreated": "2021-07-09T14:08:35.822Z"
}
```