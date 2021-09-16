from flask import Blueprint, Flask, redirect, render_template, request

from models.country import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)