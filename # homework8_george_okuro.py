# homework8_george_okuro.py
# Week 8 - Functions Assignment

# Function that accepts a list of sandwich ingredients
def make_sandwich(*ingredients):
    print("\nSandwich Order Summary")
    print("-----------------------")
    
    if len(ingredients) == 0:
        print("No ingredients selected.")
    else:
        print("Your sandwich includes:")
        for ingredient in ingredients:
            print(f"- {ingredient}")

# First sandwich order (3 ingredients)
make_sandwich("Ham", "Cheese", "Lettuce")

# Second sandwich order (6 ingredients)
make_sandwich("Turkey", "Tomato", "Onion", "Pickles", "Mayonnaise", "Mustard")