import os

from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Connect to database
conn = sqlite3.connect('dmv2u.sqlite')
cursor = conn.cursor()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Route to landing page
@app.route("/", methods=['GET', 'POST'])
def home():
	return "<h1>DMV2U API</h1><p>This site is a prototype API for Oregon DMV vanity plates.</p>"

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# Get all route
@app.route('/api/v1/plates/all', methods=['GET'])
def api_all():
	conn = sqlite3.connect('dmv2u.sqlite')
	conn.row_factory = dict_factory
	cur = conn.cursor()
	all_plates = cur.execute('SELECT * FROM dmv2u;').fetchall()
	return jsonify(all_plates)


@app.route('/api/v1/plates', methods=['GET'])
def api_filter():
	query_parameters = request.args
	id = query_parameters.get('id')
	date = query_parameters.get('date')
  string = query_parameters.get('string')
  status = query_parameters.get('status')
  make = query_parameters.get('make')
  model = query_parameters.get('model')
  year = query_parameters.get('year')
  prev_date = query_parameters.get('prev_date')
  prev_make = query_parameters.get('prev_make')
  prev_model = query_parameters.get('prev_model')
  prev_year = query_parameters.get('prev_year')	

	query = "SELECT * FROM dmv2u WHERE"
	to_filter = []

	if id:
		query += ' id=? AND'
		to_filter.append(id)
	if date:
		query += ' date=? AND'
		to_filter.append(date)
	if string:
		query += ' string=? AND'
		to_filter.append(string)
	if status:
		query += ' status=? AND'
		to_filter.append(status)
	if make:
		query += ' make=? AND'
		to_filter.append(make)
	if model:
		query += ' model=? AND'
		to_filter.append(model)
	if year:
		query += ' year=? AND'
		to_filter.append(year)
	if prev_date:
		query += ' prev_date=? AND'
		to_filter.append(prev_date)
	if prev_make:
		query += ' prev_make=? AND'
		to_filter.append(prev_make)
	if prev_model:
		query += ' prev_model=? AND'
		to_filter.append(prev_model)
	if prev_year:
		query += ' prev_year=? AND'
		to_filter.append(prev_year)
	if not (id or date or prev_date or status or string):
        return page_not_found(404)

	query = query[:-4] + ';'

	print("~~~~~~~~~~~" + query + "~~~~~~~~~~~~~")

	conn = sqlite3.connect('dmv2u.sqlite')
	conn.row_factory = dict_factory
	cur = conn.cursor()

	results = cur.execute(query, to_filter).fetchall()

	return jsonify(results)

app.run()