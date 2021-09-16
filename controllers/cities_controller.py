from flask import Blueprint, Flask, redirect, render_template, request

from models.city import City
import repositories.cities as city_repository
import repositories.counrty as counrty_repository

cities_blueprint = Blueprint("cities", __name__)