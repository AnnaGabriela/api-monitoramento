import settings
from flask import Flask, render_template, jsonify
from database.requests import getDomes, getAttributes

app = Flask(__name__)

@app.route('/cupulas')
def getCupulas():
    return jsonify(getDomes())

@app.route('/<cupula>')
def getCupula(cupula):
    return jsonify(getAttributes(cupula))

if __name__ == '__main__':
    app.run(debug=True)