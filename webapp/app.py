from flask import Flask
from flask import request, render_template
import json

app = Flask(__name__)
app.debug = True



@app.route("/")
def index():
    with open('headers.json', 'r') as f:
        tables = json.load(f)
    context = {
        'tables': [{'id': tab, 'header': tables[tab]} for tab in tables.keys()],
    }
    return render_template('index.html', context=context)

@app.route("/results", methods=['POST'])
def result():
    question = request.form['question']
    table_id = request.form['id']
    
    context = request.form
    return render_template('result.html', context=context)

@app.route("/table/<string:table_id>")
def table_id(table_id):
    with open('questions.json', 'r') as f:
        data = json.load(f)
    context = {
        'id': table_id,
        'questions': data[table_id]
    }
    return render_template('questions.html', context=context)

app.run()