from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/basket",methods=['POST'])
def basket():
    print(request.data)
    return "Success"