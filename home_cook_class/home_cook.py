from food_data_class.food import Food
from clear import clear

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
        print("Ingredients List for {name}:".format(name=self.food.food_name))
        for data in self.ingredients:
            print('\t', '- ' + data)

        print('\n\n' + "Step By Step Guide for {name}: ".format(name=self.food.food_name))
        for data in self.steps:
            print('\t', '- ' + data)

