# by Kami Bigdely
# Extract Class

class Food:
    """
    Represents a food item with complete recipe information.
    This class encapsulates all the details needed to describe and prepare a dish,
    including ingredients, cooking instructions, and dietary information.
    """
    
    def __init__(self, name, prep_time, is_veggie, food_type, cuisine, ingredients, recipe):
        """
        Initialize a Food object with complete recipe information.
        
        Args:
            name (str): Name of the food dish
            prep_time (int): Preparation time in minutes
            is_veggie (bool): True if the dish is vegetarian, False otherwise
            food_type (str): Category of food (e.g., 'soup', 'salad', 'deli')
            cuisine (str): Type of cuisine (e.g., 'North African', 'Iranian', 'All')
            ingredients (list): List of ingredients needed for the recipe
            recipe (str): Step-by-step cooking instructions
        """
        self.name = name
        self.prep_time = prep_time
        self.is_veggie = is_veggie
        self.food_type = food_type
        self.cuisine = cuisine
        self.ingredients = ingredients
        self.recipe = recipe
    
    def display(self):
        """
        Display all information about the food item in a formatted way.
        Shows name, prep time, dietary info, type, cuisine, ingredients, and recipe.
        """
        print("Name:", self.name)
        print("Prep time:", self.prep_time, "mins")
        print("Is Veggie?", 'Yes' if self.is_veggie else "No")
        print("Food Type:", self.food_type)
        print("Cuisine:", self.cuisine)
        
        # Display ingredients as a comma-separated list
        for item in self.ingredients:
            print(item, end=', ')
        print()
        
        print("Recipe", self.recipe)
        print("***")  # Separator between different recipes

# Create a collection of sample recipes demonstrating different cuisines and types
foods = [
    # North African vegetarian soup
    Food('butternut squash soup', 45, True, 'soup', 'North African',
         ['butter squash', 'onion', 'carrot', 'garlic', 'butter', 'black pepper', 'cinnamon', 'coconut milk'],
         '1. Grill the butter squash, onion, carrot and garlic in the oven until they get soft and golden on top 2. Put all in blender with butter and coconut milk. Blend them till they become puree. Then move the content into a pot. Add coconut milk. Simmer for 5 minutes.'),
    
    # Iranian vegetarian salad
    Food('shirazi salad', 5, True, 'salad', 'Iranian',
         ['cucumber', 'tomato', 'onion', 'lemon juice'],
         '1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 3. add salt 4. Mixed them thoroughly'),
    
    # Universal meat-based deli item
    Food('Home-made Beef Sausage', 60, False, 'deli', 'All',
         ['sausage casing', 'regular ground beef', 'garlic', 'coriander seeds', 'black pepper seeds', 'fennel seed', 'paprika'],
         '1. In a blender, blend coriander seeds, black pepper seeds, fennel seeds and garlic to make the seasonings 2. In a bowl, mix ground beef with the seasoning 3. Add all the content to a sausage stuffer. Put the casing on the stuffer funnel. Rotate the stuffer\'s handle (or turn it on) to make your yummy sausages!')
]

# Display all recipes in the collection
for food in foods:
    food.display()
