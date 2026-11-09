import requests


COUNTRIES_URL = "https://countries.dev/countries"
TIMEOUT = 20





def fetch_countries():
    """
    Fetches country data from the COUNTRIES_URL and returns it as a list of dictionaries.
    Raises an exception if the request fails or if the response is not valid JSON.
    """
    try:
        response = requests.get(COUNTRIES_URL, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"There was an error fetching country data: {e}")
        raise SystemExit(1)





"""
#Testing the functions
search_region = input("Enter a region name: ").strip().casefold()
search_name = input("Enter a country name: ").strip().casefold()


"""