from db.run_sql import run_sql

from models.country import Country
from models.city import City

def delete_all():
    sql = "DELETE  FROM city"
    run_sql(sql)