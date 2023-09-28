# Recipe App

This is a simple recipe app that allows a user to search for recipes by ingredient. It uses the [Spoonacular API](https://spoonacular.com/food-api) to get recipe data.

## Files

**food.py**

Contains the Food class that handles interacting with the Spoonacular API to get recipe data.

Key methods:

- `grab_food_data` - Searches for recipes by ingredient name
- `grab_food_ingredients` - Gets ingredients and instructions for a specific recipe

**home_cook.py**

Contains HomeCook class to manage recipe data and printing.

Key methods:

- `get_food_lists` - Gets recipe data from Food instance
- `print_recipe` - Prints ingredients and instructions

**main.py**

Main app code and user interaction loop.

Key components:

- User input for ingredient name
- Create HomeCook instance
- Display recipe options
- Get selected recipe data
- Print recipe
- Repeat or exit

## Setup

The Spoonacular API key is hardcoded - this should be set as an environment variable or config for security.

Install dependencies:

```
pip install -r requirements.txt
```

## Usage

Run `python main.py`

Enter an ingredient name like "chicken" to search for chicken recipes. Select a recipe to view the ingredients and instructions.

Enter "n" to exit or any key to search for another recipe.

## Next Steps

Possible enhancements:

- Add user accounts to save favorite recipes
- Improve recipe formatting for printing
- ~~Add option to print/export recipe to PDF~~
- Expand search options beyond single ingredient
