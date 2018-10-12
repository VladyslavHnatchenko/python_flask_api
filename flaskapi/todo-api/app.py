import os
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


# run this command in cmd - 'curl -i http://localhost:5000/todo/get/1'
@app.route('/todo/get/1', methods=['GET', 'POST'])
def get_json():
    return jsonify({'contacts': contacts})


@app.route('/todo/get/2', methods=['GET', 'POST'])
def get2_json():
    return jsonify({'contacts': contacts2})


@app.route('/todo/get/convert_to_json', methods=['POST', 'GET'])
def convert_to_json():
    for csv_file in glob('contacts1.csv'):
        stem, _ = splitext(csv_file)
        json_file = stem + '.json'

    with open(csv_file) as csv, open(json_file, 'w') as json:
        dump(list(DictReader(csv)), json)

    # return render_template('index.html', json_file=json_file)
    return jsonify(json_file)


@app.route('/todo/get/show_json', methods=['POST', 'GET'])
def show_json():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "", "contacts1.json")
    data = json.load(open(json_url))

    return render_template('index.html', data=data)


@app.route('/test', methods=['POST', 'GET'])
def get(url):
    r = requests.get('https://api.github.com/users/runnable')
    return jsonify(r.json())


# @app.route("/get_json_uri", methods=['GET', 'POST'])
# def get_json_uri():
#     uri = "https://eu16.lightning.force.com/lightning/o/Contact/list?filterName=Recent"
#     # uri = "https://api.stackexchange.com/2.0/users?   order=desc&sort=reputation&inname=fuchida&site=stackoverflow"
#     try:
#         uResponse = requests.get(uri)
#     except requests.ConnectionError:
#        return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#
#     return Jresponse
#
#
# @app.route('/hello', methods=['GET', 'POST'])
# def hello():
#     print("hello")
#     return jsonify(request.json)


if __name__ == '__main__':
    app.run(debug=True)
