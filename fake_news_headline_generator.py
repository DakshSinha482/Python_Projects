import random

subjects = ["Shah Rukh Khan", "MS Dhoni", "Chetan Bhagat", "Sheya Ghosal"]
actions = ["plays in", "writes a new book on life in", "travels to", "buys a new place in","visits their ancestrial home in "]
places_or_things = ["Mumbai", "Delhi", "Kolkata", "Bangalore","Chennai"]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)

    headline = f"Breaking News: {subject} {action} {place}"
    print("\n" + headline)

    user_input = input("Do you wish to continue? (yes/no): ").strip().lower()
    if user_input == "no":
        print("Exiting... Goodbye!")
        break
