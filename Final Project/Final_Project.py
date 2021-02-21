'''Recipe Application
Enter 3 recipes.
Create a separate class for each recipe.
Identify the products used in this recipe using the init() method.
Write a function about how long these products should be used later.

Use inheritance.
E.g. cooking function; it will be common to all, so inherit it.'''

class Kitchen():
    def __init__(self, ingredient, mix_time, heat_time):
        self.ingredient = ingredient
        self.mix_time = mix_time
        self.heat_time = heat_time
    
    def add(self, ingredient):
        if ingredient:
            print(f"{self.ingredient}: ekliyoruz...")
        else:
            print("Biraz ekliyoruz...")
            
    def mix(self, mix_time):
        if mix_time:
            print(f"{self.mix_time}: dakika karıştırıyoruz...")
        else:
            print("Biraz karıştırıyoruz...")
    
    def heat(self, heat_time):
        if heat_time:
            print(f"{self.heat_time}: dakika ısıtıyoruz...")
        else:
            print("Biraz ısıtıyoruz...")

#class Ingredient():
#    def __init__(self, cut)

class Menemen(Kitchen):
    def __init__(self, ingredient, mix_time, heat_time):
        super().__init__(ingredient, mix_time, heat_time)

class Pilav(Kitchen):
    def __init__(self, ingredient, mix_time, heat_time):
        super().__init__(ingredient, mix_time, heat_time)

class Puding(Kitchen):
    def __init__(self, ingredient, mix_time, heat_time):
        super().__init__(ingredient, mix_time, heat_time)

print(Menemen("Yumurta", 3, 15))
print(Pilav("Pirinç", 2, 30))
print(Puding("Puding tozu", 20, 30))
