from flask import Flask
from flask import request, render_template

app = Flask(__name__)
app.debug = True



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result", methods=['POST'])
def result():
    data = request.form
    # load the model and do the processing here
    payload = request.form
    return render_template('result.html', payload=payload)

app.run()