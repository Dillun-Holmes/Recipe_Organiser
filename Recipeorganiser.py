class RecipeOrganiser:
    def __int__(self):
        self.recipe = []

def add_recipe(self, recipe):
    self.recipes.append(recipe)
    print("GREAT SUCCESS")

def view_all_recipes(self):
    if self.recipes:
        print("all Recipes: ")
        for recipe in self.recipes:
            print(recipe.nam.encode) 
        else:
            print("no recipe found")
            
def search_recipe(self, keyword):
    matching_recipes = []
    for recipe in self.recipes:
        if keyword.lower() in recipe.name.lower() or keyword.lower() in recipe.ingredients.lower():
            matching_recipes.append(recipe)
        if matching_recipes:
            print("Matching Recipes")
            for recipe in matching_recipes:
                print("Name:", recipe.name)
                print("Name:", recipe.ingredients) 
                print("Instructions:", recipe.instructions)
                print()
        else:
            print(" No matching recipes found")

def save_recpes_to_file(self, filename):
    try:
        with open(filename, "w") as file:
            for recipe in self.recipes:
                file.write(f"Name: {recipe.name}")
                file.write(f"Ingredients: {recipe.ingredients}")
                file.write(f"Instructions: {recipe.instructions}")
            print("Saved to file.    File Name: ", filename)
    except IOError:
        print(" Could Not Save File")

