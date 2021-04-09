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

def temp(total):
    orders={}
    cb = int(0.65 * total)
    orders[0]={}
    orders[1]={}
    orders[0]["name"] = "Chicken Burger"
    orders[0]["quantity"] = cb
    orders[1]["name"] = "Veg Burger"
    orders[1]["quantity"] = total-cb
    return orders


def getInventory(orders):
    inventory={}
    for food in orders.values():
        foodID = Food_Item.objects.get(item_name=food["name"]).id
        x = Recipe.objects.filter(food=foodID)
        num = food["quantity"]

        for y in x.iterator():
            ingName = y.ingredient.ingredient_name
            j = y.ingredient.id
            quant = y.quantity * num

            if j not in inventory:
                inventory[j]={}
                inventory[j]["name"] = ingName
                inventory[j]["quantity"] = quant
                inventory[j]["unit"] = y.ingredient.ingredient_unit

            else:
                inventory[j]["quantity"] += quant

    for entries in inventory.values():
        entries["display"] = str(entries["quantity"]) + " " + entries["unit"]


    return inventory




