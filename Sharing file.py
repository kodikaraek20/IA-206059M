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
# Define a dictionary with animal names, their categories, and additional information
animal_info = {
    "cat": {
        "category": "mammal",
        "sound": "Meow",
        "habitat": "Domestic and wild",
    },
    "dog": {
        "category": "mammal",
        "sound": "Woof",
        "habitat": "Domestic and wild",
    },
    "parrot": {
        "category": "bird",
        "sound": "Squawk",
        "habitat": "Tropical regions",
    },
    "snake": {
        "category": "reptile",
        "sound": "Hiss",
        "habitat": "Various environments",
    },
    "fish": {
        "category": "fish",
        "sound": "None",
        "habitat": "Aquatic environments",
    }
}

# Prompt the user to enter the name of an animal
animal_name = input("Enter the name of an animal: ")

# Classify and provide information about the entered animal
if animal_name in animal_info:
    info = animal_info[animal_name]
    category = info["category"]
    sound = info["sound"]
    habitat = info["habitat"]
    print(f"{animal_name} is a {category}. It makes the sound '{sound}' and is found in {habitat}.")
else:
    print(f"Sorry, I don't know the category for {animal_name}.")

# You can continue to add more animals and their information to the dictionary as needed.


