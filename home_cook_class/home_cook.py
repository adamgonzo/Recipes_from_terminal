from food_data_class.food import Food
from clear import clear
import textwrap

class HomeCook:

    def __init__(self, name) -> None:
        self.food = Food(name)
        self.ingredients = []
        self.steps = []

    def get_food_lists(self):
        self.food.grab_food_data()

    def grab_food_ingredients_and_steps(self, id_for_food):
        self.ingredients, self.steps = self.food.grab_food_ingredients(id_for_food)
        clear()
        f = open('recipe.txt', 'w')

        print("Ingredients List for {name}:".format(name=self.food.food_name) + '\n')
        f.write("Ingredients List for {name}:".format(name=self.food.food_name) + '\n')
        for data in self.ingredients:
            string =  '- ' + data
            print('\n'.join(textwrap.wrap(string, width=75, replace_whitespace=True)) + '\n')
            f.write('\n'.join(textwrap.wrap(string, width=75, replace_whitespace=True)) + '\n')

        print('\n\n' + "Step By Step Guide for {name}: ".format(name=self.food.food_name) + '\n')
        f.write('\n\n' + "Step By Step Guide for {name}: ".format(name=self.food.food_name) + '\n')
        for data in self.steps:
            string =  '- ' + data
            print('\n'.join(textwrap.wrap(string, width=75, replace_whitespace=True)) + '\n')
            f.write('\n'.join(textwrap.wrap(string, width=75, replace_whitespace=True)) + '\n')

