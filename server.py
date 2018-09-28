import settings
from flask import Flask, render_template, jsonify, request
from database.requests import *

app = Flask(__name__)

@app.route('/')
def index():
    return "Projeto Ecodomo :)"

@app.route('/cupulas', methods=['GET', 'POST'])
def cupulas():
    if request.method == 'GET':
        return jsonify(getTotalDomes())
    else:
        cupula = request.form.get('cupula', None)
        return setDome(cupula)

@app.route('/cupulas/<cupula>', methods=['GET', 'POST'])
def cupula(cupula):
    if request.method == 'GET':
        return jsonify(getAttributes(cupula))
    else: 
        attribute = request.form.get('attribute', None)
        value = request.form.get('value', None)
        return setAttribute(cupula, attribute, value)

if __name__ == '__main__':
    app.run(debug=True)