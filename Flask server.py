from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/Week10_Lab-Submission")
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=50)