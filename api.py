import requests



COUNTRIES_URL = "https://countries.dev/countries"
TIMEOUT = 10



response = requests.get(COUNTRIES_URL, timeout=TIMEOUT)
countries = response.json()

print(f"Fetched {len(countries)} country records.")
if countries:
    print(countries[249])

search_region = input("Enter a region name: ").strip().casefold()
search_name = input("Enter a country name: ").strip().casefold()

for country in countries:
    if country["region"].casefold() == search_region:
        print(country["name"])
"""
for country in countries:
    if country["name"].casefold() == search_name:
        print(country)
        break
else:
    print("No country matched that name.")"""