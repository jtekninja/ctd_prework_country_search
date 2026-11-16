# Countries and Their Populations Finder by Region

This app was created for Code the Dream Pre-Work. It lets the user select a region and view the countries and their populations within that region by Sanjai Syamaprasad.

## Requirements:
Python 3
An internet connection to retrieve country data

Installation and running the app:
1) Open a terminal in the project folder.
2) Install the required packages by the following command:
python -m pip install -r requirements.txt
3) Start the app by the following command:
python main.py

## Usage:
1) The app displays a numbered list of regions.
2) Enter the number of the region you want to search.
3) The app displays the countries and their populations within that region.

If you enter invalid input, the app asks you to try again. Enter `q` at the region selection prompt to quit.

## Project Files:
1) requirements.txt - Python packages needed to run this app which is only requests
2) main.py - The starting file. Runs the app and handles the user's region selection.
3) api.py - Makes the call to the countries.dev api and returns a list of dictionaries of each country.
4) countries.py - Gets a list of unique regions and gets a list of country dictionaries within a region
5) display.py - Prints the start and end messages, region menu, and summary of countries and their populations.

## API:
This app uses Countries (countries.dev), a database of every country in the world, with data on population, area, region, languages, capital city, and more.

- Base endpoint: https://countries.dev/countries
- Documentation: https://countries.dev/docs






