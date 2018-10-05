from flask import render_template
from app import app
import ast


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/worldcup')
def worldcup():
    return render_template('foot.html')


@app.route('/countries')
def countries():
    with open('app/data.txt', 'r') as f:
        countries_data = f.read()
    countries_data = ast.literal_eval(countries_data)
    return render_template('countries.html', countries_data=countries_data)
