import ast

from flask import render_template
from app import app

from app.group import default_teams
from app.results import final_stage_games


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/worldcup')
def worldcup():
    results = final_stage_games(default_teams)
    return render_template('foot.html', results=results)


@app.route('/countries')
def countries():
    with open('app/data.txt', 'r') as f:
        countries_data = f.read()
    countries_data = ast.literal_eval(countries_data)
    return render_template('countries.html', countries_data=countries_data)
