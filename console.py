import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository


city_repository.delete_all()
country_repository.delete_all()

country1 = Country('Spain', 'Europe', 'Spanish')
country_repository.save(country1)
country2 = Country('Portugal', 'Europe', 'Portuguese')
country_repository.save(country2)

# print(country_repository.save(country1))
print(country_repository.save(country2))

# print(country_repository.select_all())

# print(country_repository.select(country1.id))

pdb.set_trace()