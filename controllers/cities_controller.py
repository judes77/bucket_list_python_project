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