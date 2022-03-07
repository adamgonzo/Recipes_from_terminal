
class Food:
    def __init__(self, food) -> None:
        self.food_name = food
        self.food_data = {}

    def grab_food_data(self) -> dict:
        import requests

        response = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?sort=popularity&query={self.food_name}&number=10&apiKey=b5c2d5a202dc422a8dfd5a5266a95843")
        data = response.json()['results']
        for j in range(len(data)):
            self.food_data[data[j]['title']] = data[j]['id']

        return self.food_data

    def grab_food_ingredients(self, id_for_food) -> tuple:
        import requests
        food_data_url = f"https://api.spoonacular.com/recipes/{id_for_food}/information?includeNutrition=false&apiKey=b5c2d5a202dc422a8dfd5a5266a95843"
        food_steps_url = f"https://api.spoonacular.com/recipes/{id_for_food}/analyzedInstructions?apiKey=b5c2d5a202dc422a8dfd5a5266a95843"

        response_for_food = requests.get(food_data_url)
        response_for_steps = requests.get(food_steps_url)
        food_data = response_for_food.json()
        data_for_steps = response_for_steps.json()
        steps_data = data_for_steps[0]['steps']
        ingredients = food_data['extendedIngredients']
        ingredients_for_food = []
        steps_for_food = []
        for dat in ingredients:
            ingredients_for_food.append(dat['original'] + '\n')
        total = 0
        for j in range(len(steps_data)):
            steps_for_food.append(steps_data[j]['step'])

        return ingredients_for_food, steps_for_food
