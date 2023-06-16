from Recipe import Recipe
from Recipeorganiser import RecipeOrganiser

#display menu

def main_menu():
    print("Recipe Organizer")
    print("1. Add Recipe")
    print("2. View all Recipes ")
    print("3. Search Recipes")
    print("4. Save Recipes to File")
    print("5. Quit")

def get_main_menu():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > 5:
                raise ValueError
            return choice
        except ValueError:
            print ("Invalid Choice. Please enter a number between 1 and 5. ")

def get_recipe_details():
    name = input("Enter recipe Name")
    ingredients = input("Enter ingredients")
    instructions= input("Enter instructions")
    return Recipe (name, ingredients, instructions)

def main():
    organiser = RecipeOrganiser()
    while True:
        main_menu()
        choice = get_main_menu()
        if choice == 1:
            recipe = get_recipe_details()
            organiser.add_recipe(recipe)
        elif choice == 2:
            organiser.view_all_recipes()
        elif choice == 3:
            keyword = input("Enter a Keyword to search for:")
            organiser.search_recipe(keyword)
        elif choice == 4:
            filename = input("Enter the file name where recipes will be saved at:")
            organiser.save_recipes_to_file(filename)
        elif choice == 5:
            print("Cheers vir eers")
            break
        

main ()          
                                                           

