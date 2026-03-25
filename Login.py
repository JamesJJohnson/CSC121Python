class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0   # NEW ATTRIBUTE

    def describe_user(self):
        print(f"\nUser Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    # NEW METHOD
    def increment_login_attempts(self):
        self.login_attempts += 1

    # NEW METHOD
    def reset_login_attempts(self):
        self.login_attempts = 0


# Create an instance of User
user = User("James", "Smith", 28, "North Carolina")

# Call increment_login_attempts() several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print login_attempts to verify increments
print(f"\nLogin attempts: {user.login_attempts}")

# Reset login attempts
user.reset_login_attempts()

# Print again to verify reset
print(f"Login attempts after reset: {user.login_attempts}")

