from .models import Food_Item, Ingredient, Recipe
import django.db

def addItem(food, recipe):
    f = ""  
    if not Food_Item.objects.filter(item_name=food).exists():
        f = Food_Item(item_name=food)
        f.save()
    
    else:
        f=Food_Item.objects.get(item_name=food)

    for ing, measurement in recipe.items():  
        i=""      
        if not Ingredient.objects.filter(ingredient_name=ing).exists():
            i = Ingredient(ingredient_name=ing)
            i.save()

        else:
            i=Ingredient.objects.get(ingredient_name=ing)

        if not Recipe.objects.filter(food=f, ingredient=i).exists():
            a = Recipe(food=f, ingredient=i, quantity=measurement["quantity"] )
            a.save()

    