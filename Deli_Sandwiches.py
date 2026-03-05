sandwich_orders = ['tuna', 'ham', 'turkey', 'roast beef', 'veggie']
finished_sandwiches = []

# Make each sandwich
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# List all finished sandwiches
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")

