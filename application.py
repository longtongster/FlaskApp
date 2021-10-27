
from flask import Flask, request, render_template

application = Flask(__name__)

@application.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')

@application.route('/submit', methods=["POST","GET"])
def submit():
    return "The submit method results in a POST request"

if __name__=="__main__":
    application.run(debug=True)