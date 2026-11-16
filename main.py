from api import fetch_countries
from countries import fetch_regions,fetch_region_countries
from display import start, end, format_summary


countries = fetch_countries()
regions = fetch_regions(countries)

# Print start message and display regions
start(regions)

# Get user input for region selection and validate it
while True:
    try:
        choice = input(f"\nEnter your choice (1-{len(regions)}) or 'q' to quit: ").strip().casefold()
        if choice == "q":
            break
        elif int(choice) >= 1 and int(choice) <= len(regions):
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 8, or 'q' to quit.")
    except ValueError:
        print("\nInvalid input. Please enter a whole number between 1 and 8, or 'q' to quit.")

format_summary(fetch_region_countries(countries, regions[int(choice)-1]), regions[int(choice)-1]) 

# Print end message
end()
