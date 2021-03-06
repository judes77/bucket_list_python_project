from db.run_sql import run_sql
from controllers.countries_controller import countries
from flask import Blueprint, Flask, redirect, render_template, request

from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

# INDEX
@cities_blueprint.route('/cities')
def cities():
    cities = city_repository.select_all()
    return render_template('cities/index.html', all_cities = cities)

# NEW
@cities_blueprint.route('/cities/new')
def new_city():
   countries = country_repository.select_all()
   return render_template('cities/new.html', all_countries = countries) 

# CREATE
@cities_blueprint.route('/cities', methods=['POST'])
def create_city():
    name = request.form['name']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, country, visited)
    city_repository.save(city)
    return redirect('/cities')

# SHOW
@cities_blueprint.route('/cities/<id>', methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template('cities/show.html', city = city)

# EDIT
@cities_blueprint.route('/cities/<id>/edit')
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('cities/edit.html', city = city, all_countries = countries)

# UPDATE
@cities_blueprint.route('/cities/<id>', methods=['POST'])
def update_city(id):
    name = request.form['name']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, country, visited, id)
    city_repository.update(city)
    return redirect ('/cities')

# DELETE
@cities_blueprint.route('/cities/<id>/delete', methods=['POST'])
def delete_cities(id):
    city_repository.delete(id)
    return redirect('/cities')