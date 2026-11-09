import requests



COUNTRIES_URL = "https://countries.dev/countries"
TIMEOUT = 20


try:
    response = requests.get(COUNTRIES_URL, timeout=TIMEOUT)
    response.raise_for_status()
    countries = response.json()
except requests.exceptions.RequestException as e:
    print(f"There was an error fetching country data: {e}")
    raise SystemExit(1)

search_region = input("Enter a region name: ").strip().casefold()
#search_name = input("Enter a country name: ").strip().casefold()


def fetch_regions():
    # Fetch and return a sorted list of unique regions.
    regions= set()

    for country in countries:
        regions.add(country.get("region", ""))

    return sorted(regions)



def fetch_region_countries(region_name):
    # Fetch and return a list of countries within the region.
    matching_countries=[]

    for country in countries:
        if country.get("region", "").casefold() == region_name.strip().casefold():    
            matching_countries.append(country)
    return matching_countries

def search_population(country_name):
    # Return the population of the country.
    for country in countries:
        if country["name"].casefold() == country_name.strip().casefold():
            return country["population"]
    return None

#Testing the functions
print(len(fetch_region_countries(search_region)))
print(fetch_regions())
print(search_population("India"))