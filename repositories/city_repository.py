from db.run_sql import run_sql

from models.city import City
from models.country import Country
import repositories.country_repository as country_repository

def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)