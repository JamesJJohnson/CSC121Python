def describe_city(city, country="USA"):
    """Print a simple sentence describing a city and its country."""
    print(f"{city.title()} is in {country}.")

# Calling the function for three cities
describe_city("new york")        # uses default country
describe_city("los angeles")     # uses default country
describe_city("tokyo", "Japan")  # overrides default

