from api import fetch_countries
from countries import fetch_regions, fetch_country_population, fetch_region_countries
#from display import display_countries

countries = fetch_countries()
region = input("Enter a region: ")


print(len(fetch_region_countries(countries,region)))
print(fetch_regions(countries))
print(fetch_country_population(countries,"India"))