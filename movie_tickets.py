# 7-5. Movie Tickets

print("Welcome to the Movie Ticket Calculator!")

# Ask how many tickets the user needs
num_tickets = int(input("How many tickets do you need? "))

total_cost = 0

# Loop through each ticket holder
for i in range(num_tickets):
    age = int(input(f"Enter the age of person #{i + 1}: "))

    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    total_cost += price

# Final total
print(f"\nThe total cost for your tickets is: ${total_cost}")

