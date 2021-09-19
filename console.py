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
country3 = Country('Scotland', 'Europe', 'English')
country_repository.save(country3)

city1 = City('Edinburgh', country3)
city_repository.save(city1)
city2 = City('Barcelona', country1)
city_repository.save(city2)

# print(country_repository.save(country1))
# print(country_repository.save(country2))

# print(country_repository.select_all())

# print(country_repository.select(country1.id))
# print(city_repository.select_all())

# print(city_repository.save(city1))



pdb.set_trace()