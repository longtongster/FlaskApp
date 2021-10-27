
from flask import Flask, request, render_template

application = Flask(__name__)

@application.route('/', methods=["GET","POST"])
def index():
    return "<h1>Flask application is running</h1>"

if __name__=="__main__":
    application.run(debug=True)