from api import fetch_countries
from countries import fetch_regions,fetch_region_countries
from display import start, end, format_summary


countries = fetch_countries()

if not countries:
    print("No country data was fetched. Exiting the program.\n")
    raise SystemExit(1)

regions = fetch_regions(countries)

# This will loop until the user chooses to quit by entering 'q'.
while True:
    # Print start message and display regions
    start(regions)

    # Get user input for region selection and validate it
    choice = input(f"\nEnter your choice (1-{len(regions)}) or 'q' to quit: ").strip().casefold()
    
    if choice == "q":
            break
      
    try:
        region_number = int(choice)
    
    except ValueError:
        print("Invalid input. Enter a whole number or 'q' to quit.")
        continue

    if region_number < 1 or region_number > len(regions):
        print(f"Invalid choice. Enter a number from 1 to {len(regions)}.")
        continue

    region = regions[region_number - 1]
    matching_countries = fetch_region_countries(countries, region)

    if matching_countries:
        format_summary(matching_countries, region)
    else:
        print(f"No countries were found in {region}.")

# Print end message
end()
