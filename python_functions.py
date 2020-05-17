from matplotlib import pyplot as plt
import requests
import json
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


<<<<<<< HEAD
=======
matplotlib.use("TKAgg")
>>>>>>> 03b757287fc035bd60ab4d619cbf11d7a2bcb50e

# gets data as a string when given main ingredient and number


def get_data_string(ingredient, number):
    apiKey = "851e31b033fb47518e40cbd5a6b6019a"
    url = f"https://api.spoonacular.com/recipes/search?query={ingredient}&number={number}&apiKey={apiKey}"

    return {"results": [{"id": 215435, "title": "Three-Cheese Pizza (For Cheese Lovers)", "readyInMinutes": 45, "servings": 8, "sourceUrl": "http://www.myrecipes.com/m/recipe/three-cheese-pizza-for-cheese--50400000110662/", "openLicense": 0, "image": "three-cheese-pizza-for-cheese-lovers-215435.jpg"}, {"id": 323420, "title": "Grilled Cheese", "readyInMinutes": 55, "servings": 4, "sourceUrl": "http://www.foodnetwork.com/recipes/tyler-florence/grilled-cheese-recipe.html", "openLicense": 0, "image": "grilled-cheese-323420.jpeg"}], "baseUri": "https://spoonacular.com/recipeImages/", "offset": 0, "number": 2, "totalResults": 851, "processingTimeMs": 454, "expires": 1589681250164, "isStale": "apple"}
    # return json.loads(requests.get(url).content.decode('utf-8'))

# gets id_list from a dictionary in a list for 'results'


def get_data_list(python_data):
    data_list = python_data['results']
    id_list = []
    for index in range(len(data_list)):
        id_list += [(data_list[index]['id'])]
    return id_list


# gets nutrition facts from recipe ID
def get_nutrition_facts(id):
    #url = f"https://api.spoonacular.com/recipes/{str(id)}/nutritionWidget.json?apiKey={apiKey}"
    # return json.loads(requests.get(url).content.decode('utf-8'))
    return {"calories": "316", "carbs": "49g", "fat": "12g", "protein": "3g", "bad": [{"amount": "316", "indented": "apple"}]}

# returns calories and nutrition list


def get_nutrition_list(nutritionFacts):
    calories = float(nutritionFacts['calories'])
    carbs = float(nutritionFacts['carbs'].replace('g', ""))
    fat = float(nutritionFacts['fat'].replace('g', ""))
    protein = float(nutritionFacts['protein'].replace('g', ""))
    return(calories, [carbs, fat, protein])

# gets the recipe name from ID


def get_recipe_name(id):
    #url = f"https://api.spoonacular.com/recipes/{id}/information?includeNutrition=false&apiKey={apiKey}"
    #information = json.loads(requests.get(url).content.decode('utf-8'))
    # return information['title']
    return 145193

# displays a pie chart of calories, name, and nutritional info


def plot_pie_chart(title, calories, sizes):

    labels = 'carbs', 'fat', 'protein'
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0, 0, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.title(f"{title} ({calories} kcal)")
    plt.show()
    plt.savefig('plot.png')


def get_customized_recipe_ID_list():
    #minCarbs = input("Please enter minimum carbs (if none, enter 0): ")
    #maxCarbs = input("Please enter maximum carbs (if none, enter 0): ")
    # input("Please enter minimum calories (if none, enter 0): ")
    minCalories = 100
    # input("Please enter maximum calories (if none, enter 0): ")
    maxCalories = 460
    #minProteins = input("Please enter minimum proteins (if none, enter 0): ")
    #maxProteins = input("Please enter maximum proteins (if none, enter 0): ")
    #minFats = input("Please enter minimum fats (if none, enter 0): ")
    #maxFats = input("Please enter maximum fats (if none, enter 0): ")
    number = 1  # input("How many recipes would you like?: ")

    #url = f"https://api.spoonacular.com/recipes/findByNutrients?minCarbs={minCarbs}&maxCarbs={maxCarbs}&minCalories={minCalories}&maxCalories={maxCalories}&minProteins={minProteins}&maxProteins={maxProteins}&minFats={minFats}&maxFats={maxFats}&number={number}&apiKey={apiKey}"
    #url = f"https://api.spoonacular.com/recipes/findByNutrients?minCalories={minCalories}&maxCalories={maxCalories}&number={number}&apiKey={apiKey}"
    #options = json.loads(requests.get(url).content.decode('utf-8'))
    # options_list=[]

    # for index in range(len(options)):
    #options_list += [(options[index]["id"])]

    return [145193]  # options_list

# ingredient = "potato"  # input("Please enter ingredient: ")
# number = 1  # int(input("Please enter number of searches: "))

#python_data = get_data_string(ingredient, number)
#id_list = get_data_list(python_data)

# for index in range(len(id_list)):
    #nutrition_facts = get_nutrition_facts(id_list[index])
    #calories, nutrition_list = get_nutrition_list(nutrition_facts)
    #title = get_recipe_name(id_list[index])
    #plot_pie_chart(title, calories, nutrition_list)

#customized_list = get_customized_recipe_ID_list()
# for index in range(len(customized_list)):
#    nutrition_facts = get_nutrition_facts(customized_list[index])
#   calories, nutrition_list = get_nutrition_list(nutrition_facts)
#    title = get_recipe_name(customized_list[index])
#   plot_pie_chart(title, calories, nutrition_list)
