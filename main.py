from home_cook_class.home_cook import HomeCook
from clear import clear
from fpdf import FPDF
import os

if __name__ == '__main__':
    import pyfiglet
    txt = "Recipes For You"
    terminal_txt = pyfiglet.figlet_format(txt, font="doom", justify="center")
    print(terminal_txt)



    while True:
        name_of_food = input("Please enter ingredients for the food you would like to make if more than one ingredient seperate by comma(ex: kale, shrimp, salmon, etc)\n\n: ").strip(' ')
        clear()

        cook = HomeCook(name_of_food)

        data_for_food = cook.food.grab_food_data()

        choices = {}
        counter = 1

        for key, value in data_for_food.items():
            choices[counter] = [key, value]
            counter += 1

        if len(data_for_food) == 0:
            print("No recipes found please enter different ingredients")
            done = False
            while True:
                choice = input("Would you like to look up another recipe Yes(y or Y) No(n or N) ?")

                if choice.lower() == 'y':
                    clear()
                    break

                elif choice.lower() == 'n':
                    clear()
                    print("Have a good day!")
                    done = True
                    break
                else:
                    print("Please enter a choice that is available")
                    continue

            if done == True:
                break
            elif (len(data_for_food) == 0 and done == False):
                continue

        print("Here is the top {total} recipes for {name}:".format(name=name_of_food, total=len(data_for_food)))
        for i, key in enumerate(data_for_food.keys()):
            print('\t', str(i+1) + ': ' + key)

        choice = input("\nPlease enter choice 1-10 or (b or B) for Back to try something else: ")
        if choice.isdigit():
            choice = int(choice)
        else:
            if choice.lower() == 'b':
                clear()
                continue
        clear()

        cook.grab_food_ingredients_and_steps(choices[choice][1], choices[choice][0])

        
        end = input("\nPlease enter (n or N) to exit or (y or Y) to try another reciepe or press (p or P) for pdf of reciepe: " )
        if end.lower() == 'n':
            exit()
        elif end.lower() == 'y':
            clear()
            continue
        else:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=15)
            f = open('recipe.txt', 'r')
            for x in f:
                pdf.cell(200, 10, txt=x, ln = 10, align='C')
            pdf.output('reciepe_final.pdf')
            os.remove('recipe.txt')
            clear()
            break


