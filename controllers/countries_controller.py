from typing import ValuesView
from db.run_sql import run_sql
from itertools import count
import re
from flask import Blueprint, Flask, redirect, render_template, request

from models.country import Country
# import repositories.country_repository as country_repository
from repositories import country_repository
countries_blueprint = Blueprint("countries", __name__)


# INDEX
@countries_blueprint.route('/countries')
def countries():
    countries = country_repository.select_all()
    return render_template('countries/index.html', all_countries = countries)

# NEW
@countries_blueprint.route('/countries/new')
def new_country():
    new_country = country_repository.select_all()
    return render_template('/countries/new.html', country = new_country)

# CREATE
@countries_blueprint.route('/countries', methods=['POST'])
def create_country():
    name = request.form['name']
    continent = request.form['continent']
    language = request.form['language']
    country = Country(name, continent, language)
    country_repository.save(country)
    return redirect('/countries')

# SHOW
@countries_blueprint.route('/museums/<id>', methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country = country)

# EDIT
@countries_blueprint.route('/countries/<id>/edit')
def edit_country(id):
    country = country_repository.select(id)
    return render_template('countries/edit.html', country = country)

# UPDATE
@countries_blueprint.route('/countries/<id>', methods=['POST'])
def update_country(id):
    name = request.form['name']
    continent = request.form['continent']
    language = request.form['language']
    country = Country(name, continent, language, id)
    country_repository.update(country)
    return redirect('/countries')

# DELETE

def delete_all(id):
    sql = "DELETE  FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DELETE ONE
@countries_blueprint.route('/countries/<id>/delete', methods=['POST'])
def delete(id):
    country_repository.delete(id)
    return redirect('/countries')
