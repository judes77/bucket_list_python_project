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
country4 = Country('England', 'Europe', 'English')
country_repository.save(country4)
country5 = Country('New Zealand', 'Oceania', 'English')
country_repository.save(country5)
country6 = Country('Austrlia', 'Australia', 'English')
country_repository.save(country6)
country7 = Country('Usa', 'Americas', 'English')
country_repository.save(country7)
country8 = Country('Portugal', 'Europe', 'Portuguese')
country_repository.save(country8)
country9 = Country('France', 'Europe', 'English')
country_repository.save(country9)
country10 = Country('England', 'Europe', 'English')
country_repository.save(country10)
country11 = Country('New Zealand', 'Oceania', 'English')
country_repository.save(country11)
country12 = Country('Austrlia', 'Australia', 'English')
country_repository.save(country12)

city1 = City('Edinburgh', country3)
city_repository.save(city1)
city2 = City('Barcelona', country1)
city_repository.save(city2)
city3 = City('Nairn', country3)
city_repository.save(city3)
city4 = City('London', country4)
city_repository.save(city4)
city5 = City('Auckland', country5)
city_repository.save(city5)
city6 = City('Sydney', country6)
city_repository.save(city6)
city7 = City('New York', country7)
city_repository.save(city7)
city8 = City('Paris', country8)
city_repository.save(city8)





pdb.set_trace()