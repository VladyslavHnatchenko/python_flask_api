import os
from sqlite3 import DatabaseError

import requests

from flask import Flask, render_template, json
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from csv import DictReader
from glob import glob
from json import dump
from os.path import splitext


app = Flask(__name__)


contacts = [{"Salutation": "-", "First Name": "Stepann", "Last Name": "Banderaa", "Title": "-", "Mailing Street": "One Market St \n\nSuite 300", "Mailing City": "San Francisco", "Mailing State/Province": "CA", "Mailing Zip/Postal Code": "94105", "Mailing Country": "USA", "Phone": "(38098) 787-2230", "Mobile": "-", "Fax": "-", "Email": "stepann@test.com", "Account Owner": "Vladyslav Hnatchenko", "Account Name": "salesforce.com (Sample)"}, {"Salutation": "-", "First Name": "Tarass", "Last Name": "Shevchenkoo", "Title": "-", "Mailing Street": "One Market St \n\nSuite 300", "Mailing City": "San Francisco", "Mailing State/Province": "CA", "Mailing Zip/Postal Code": "94105", "Mailing Country": "USA", "Phone": "(38098) 787-2228", "Mobile": "-", "Fax": "-", "Email": "tarass@test.com", "Account Owner": "Vladyslav Hnatchenko", "Account Name": "salesforce.com (Sample)"}, {"Salutation": "-", "First Name": "Andriii", "Last Name": "Lysenkoo", "Title": "-", "Mailing Street": "One Market St \n\nSuite 300", "Mailing City": "San Francisco", "Mailing State/Province": "CA", "Mailing Zip/Postal Code": "94105", "Mailing Country": "USA", "Phone": "(38098) 787-2229", "Mobile": "-", "Fax": "-", "Email": "andriii@test.com", "Account Owner": "Vladyslav Hnatchenko", "Account Name": "salesforce.com (Sample)"}, {"Salutation": "Grand Totals (3 records)", "First Name": "Grand Totals (3 records)", "Last Name": "Grand Totals (3 records)", "Title": "Grand Totals (3 records)", "Mailing Street": "Grand Totals (3 records)", "Mailing City": "Grand Totals (3 records)", "Mailing State/Province": "Grand Totals (3 records)", "Mailing Zip/Postal Code": "Grand Totals (3 records)", "Mailing Country": "Grand Totals (3 records)", "Phone": "Grand Totals (3 records)", "Mobile": "Grand Totals (3 records)", "Fax": "Grand Totals (3 records)", "Email": "Grand Totals (3 records)", "Account Owner": "Grand Totals (3 records)", "Account Name": "Grand Totals (3 records)"}, {"Salutation": "", "First Name": "", "Last Name": "", "Title": "", "Mailing Street": "", "Mailing City": "", "Mailing State/Province": "", "Mailing Zip/Postal Code": "", "Mailing Country": "", "Phone": "", "Mobile": "", "Fax": "", "Email": "", "Account Owner": "", "Account Name": ""}]
contacts2 = [{"Last Name": "Shevchenkoo", "First Name": "Tarass", "Phone": "(38098) 787-2228", "Email": "tarass@test.com"}, {"Last Name": "Lysenkoo", "First Name": "Andriii", "Phone": "(38098) 787-2229", "Email": "andriii@test.com"}, {"Last Name": "Banderaa", "First Name": "Stepann", "Phone": "(38098) 787-2230", "Email": "stepann@test.com"}]


# 1 run this command in cmd - 'curl -i http://localhost:5000/todo/api/get/1'
@app.route('/todo/api/get/1', methods=['GET'])
def get_json():
    return jsonify({'contacts': contacts})


# 1.1 run this command in cmd - 'curl -i http://localhost:5000/todo/api/get/2'
@app.route('/todo/api/get/2', methods=['GET'])
def get2_json():
    return jsonify({'contacts': contacts2})


# 2 run this command in cmd - 'curl -i http://localhost:5000/todo/api/get/convert_to_json'
@app.route('/todo/api/get/convert_to_json', methods=['GET', 'POST'])
def convert_to_json():
    for csv_file in glob('contacts2.csv'):
        stem, _ = splitext(csv_file)
        json_file = stem + '.json'

    with open(csv_file) as csv, open(json_file, 'w') as json:
        dump(list(DictReader(csv)), json)

    return jsonify(json_file)


# 3 run this command in cmd - 'curl -i http://localhost:5000/todo/api/get/show_json'
@app.route('/todo/api/get/show_json', methods=['GET', 'POST'])
def show_json():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "", "contacts2.json")
    data = json.load(open(json_url))

    return jsonify(data)


# 4 run this command in cmd - 'curl -i http://localhost:5000/todo/api/send_json'
@app.route('/todo/api/send_json', methods=['GET', 'POST'])
def send_json():
    pass


# 5 run this command in cmd - 'curl -i http://localhost:5000/todo/api/post_json'
@app.route('/todo/api/post_json', methods=['GET', 'POST'])
def post_json():
    r = requests.get('http://localhost:5000/todo/api/get/2')
    return jsonify(r.json())


# function - 'This page does not exist'
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


# function - 'Database connection failed'
@app.errorhandler(DatabaseError)
def special_exception_handler(error):
    return 'Database connection failed', 500


@app.route('/')
def index():
    return "What's up, Man!"


@app.route('/hello')
def hello():
    return 'Hello, World'


if __name__ == '__main__':
    app.run(debug=True)
