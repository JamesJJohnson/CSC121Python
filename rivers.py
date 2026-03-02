rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "mississippi": "united states"
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()  # blank line for readability

# Print the name of each river
print("Rivers included in the dictionary:")
for river in rivers.keys():
    print(river.title())

print()

# Print the name of each country
print("Countries included in the dictionary:")
for country in rivers.values():
    print(country.title())

