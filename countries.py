




def fetch_regions(countries):
    # Fetch and return a sorted list of unique regions.
    regions= set()

    for country in countries:
        regions.add(country.get("region", ""))

    return sorted(regions)





def fetch_country_population(countries, country_name):
    # Return the population of the country.
    for country in countries:
        if country["name"].casefold() == country_name.strip().casefold():
            return country["population"]
    return None






def fetch_region_countries(countries, region_name):
    # Fetch and return a list of countries within the region.
    matching_countries=[]

    for country in countries:
        if country.get("region", "").casefold() == region_name.strip().casefold():    
            matching_countries.append(country)
    return matching_countries