from flask import Flask, redirect, url_for, render_template, flash, request, jsonify
from DB_interface.DB_interface import DatabaseConnection
from flask_cors import CORS
import json
import clearbit
import config
app = Flask(__name__)
CORS(app)
# REPLACE WITH THE DB INTERFACE
DB = DatabaseConnection()
clearbit.key = config.clearbit_api_key

"""
APIs:
Get all companies:
    GET /api/companies
Add a new company:
    POST /api/companies
Get postings and metadata for company:
    GET /api/companies/<COMPANY_ID>/
Add a posting for a company:
    POST /api/companies/<COMPANY_ID>
Get reviews for a position:
    GET /api/companies/<COMPANY_ID>/position/<POSITION_ID>
Post a review for a company:
    POST /api/companies/<COMPANY_ID>/position/<POSITION_ID>
"""

@app.route('/companies', methods=['GET', 'POST'])
def get_companies():
    print(request)
    if request.method == 'POST':
        form = request.json
        logo = clearbit.NameToDomain.find(name=form["name"])
        if logo is not None:
            form = {**form, **logo}
        DB.add_new_company(form)
        return jsonify(message="Company added"), 200
    else:
        company_data = DB.get_all_companies()
        return jsonify(message="Found {} companies".format(len(company_data)), data=company_data), 200

@app.route('/companies/<string:company_id>', methods=['GET', 'POST'])
def get_postings(company_id):
    if request.method == 'POST':
        form = request.json
        DB.add_new_posting(company_id, form)
        return jsonify(message="Posting added"), 200
    else:
        DB.get_all_postings_for_company(company_id)
        company_data = DB.get_all_postings_for_company(company_id)
        return jsonify(message="Found {} postings".format(len(company_data)), data=company_data), 200

@app.route('/companies/<string:company_id>/position/<string:position_id>', methods=['GET', 'POST'])
def get_reviews(company_id, position_id):
    print(company_id, position_id)
    if request.method == 'POST':
        form = request.json
        DB.add_new_review(company_id, position_id, form)
        return jsonify(message="Review added"), 200
    else:
        company_data = DB.get_all_reviews_for_posting(position_id)
        return jsonify(message="Found {} postings".format(len(company_data)), data=company_data), 200   




if __name__ == "__main__":
    app.run(host= 'localhost', port=5000)