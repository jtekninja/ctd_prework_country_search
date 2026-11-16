def fetch_regions(countries):
    # Fetch and return a sorted list of unique regions.
    regions= set()

    for country in countries:
        regions.add(country.get("region", ""))

    return sorted(regions)


def fetch_region_countries(countries, region):
    # Fetch and return a list of countries within the region.
    matching_countries=[]

    for country in countries:
        if country.get("region", "").casefold() == region.strip().casefold():    
            matching_countries.append(country)
    return matching_countries