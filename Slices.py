guest_list = ["James", "Ava", "Michael", "Sophia"]

print("Great news! I found a bigger dinner table, so more guests can join us!\n")

# Add three new guests
guest_list.insert(0, "Olivia")          # beginning
middle_index = len(guest_list) // 2
guest_list.insert(middle_index, "Liam") # middle
guest_list.append("Emma")               # end

# Sort the list alphabetically
guest_list.sort()

# Print updated invitations
print("Updated Guest List (Alphabetical Order):")
for guest in guest_list:
    print(f"Hello {guest}, you are invited to dinner!")

# -----------------------------
# 4-10 SLICES SECTION STARTS HERE
# -----------------------------

print("\nThe first three items in the list are:")
print(guest_list[:3])

print("\nThree items from the middle of the list are:")
middle_start = len(guest_list) // 2 - 1
print(guest_list[middle_start:middle_start + 3])

print("\nThe last three items in the list are:")
print(guest_list[-3:])













