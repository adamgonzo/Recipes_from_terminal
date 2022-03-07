from home_cook_class.home_cook import HomeCook
from clear import clear

if __name__ == '__main__':
    from art import tprint
    tprint("Recipes For You!")

    while True:
        name_of_food = input("Please enter type of food you would like to make (ex: kale, shrimp, salmon, etc): ")
        clear()
        cook = HomeCook(name_of_food)
        data_for_food = cook.food.grab_food_data()
        choices = {}
        counter = 1
        for key, value in data_for_food.items():
            choices[counter] = [key, value]
            counter += 1
        print("Here is the top 10 recipes for {name}:".format(name=name_of_food))
        for i, key in enumerate(data_for_food.keys()):
            print('\t', str(i+1) + ': ' + key)

        choice = int(input("Please enter choice 1-10: "))
        clear()
        cook.grab_food_ingredients_and_steps(choices[choice][1])
        end = input("\nPlease enter (n or N) to exit or (y or Y) to try another reciepe: " )
        if end.lower() == 'n':
            exit()
        else:
            clear()
            continue
        







