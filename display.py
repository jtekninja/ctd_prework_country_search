Start = "This app will show you the country names and their populations by selected region! "
Search_Region = "Please select 1-8 for your region of choice: "
End = "Thank you for using the Region Search App! "

def start(regions):
    # Prints a welcome message and displays the list of regions.
    print(f"\n{Start}\n")
    print(f"{Search_Region}\n")

    for i in range(len(regions)):
        print(f"{i+1}. {regions[i]}")

def end():
    # Prints an end message.
    print(f"\n{End}\n")



def format_summary(countries, region):
    # Prints a formatted summary of countries and their populations.
    summary_lines = []
    for country in countries:
        name = country.get("name", "Unknown")
        population = country.get("population", "Unknown")
        summary_lines.append(f"{name:<60} {population}")

   
    print(f"\nSummary of countries and populations within {region}: \n")
    print(f"{'Country Name':<60} {'Population'}")
    print("-" * 80)

    for line in summary_lines:
        print(line)
  