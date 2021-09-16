from flask import Blueprint, Flask, redirect, render_template, request

from models.counrty import counrty
import repositories.counrty_repository as counrty_repository

countries_blueprint = Blueprint("countries", __name__)