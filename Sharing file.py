# Define a dictionary with animal names and their categories
animal_categories = {
    "cat": "mammal",
    "dog": "mammal",
    "parrot": "bird",
    "snake": "reptile",
    "fish": "fish",
}

# Prompt the user to enter an animal name
animal_name = input("Enter the name of an animal: ")

# Classify the entered animal
if animal_name in animal_categories:
    category = animal_categories[animal_name]
    print(f"{animal_name} is a {category}.")
else:
    print(f"Sorry, I don't know the category for {animal_name}.")

# You can continue to add more animals and categories to the dictionary as needed.
