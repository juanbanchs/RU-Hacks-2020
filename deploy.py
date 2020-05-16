from flask import Flask, json
import requests
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def index():

    data = json.loads(requests.get(
        "https://api.spoonacular.com/recipes/search?query=potato&number=2&apiKey=851e31b033fb47518e40cbd5a6b6019a").content.decode('utf-8'))

    data 2 = json.loads({"results": [{"id": 310822, "title": "Potato Cauliflower Parsnip Soup with a Pancetta Potato Hash", "readyInMinutes": 90, "servings": 4, "sourceUrl": "http://www.foodnetwork.com/recipes/nikki-dinki/potato-cauliflower-parsnip-soup-with-a-pancetta-potato-hash-recipe.html", "openLicense": 0, "image": "potato-cauliflower-parsnip-soup-with-a-pancetta-potato-hash-310822.jpeg"}, {"id": 202914, "title": "Smoky Sweet Potato Mashed Potato Bake", "readyInMinutes": 50, "servings": 8, "sourceUrl": "http://www.myrecipes.com/recipe/smoky-mashed-sweet-potato-bake-50400000118033/", "openLicense": 0, "image": "smoky-sweet-potato-mashed-potato-bake-202914.jpg"}], "baseUri": "https://spoonacular.com/recipeImages/", "offset": 0, "number": 2, "totalResults": 851, "processingTimeMs": 424, "expires": 1589872815358, "isStale": false})
    # potato = "Hi"
    potato = "hi

    ###############################################################################################

    def get_data_string(ingredient, number):
        apiKey = "0e3889c6bf0c4b98b9e030238f39e8bf"
        url = f"https://api.spoonacular.com/recipes/search?query={ingredient}&number={number}&apiKey={apiKey}"
        import requests
        import json

        return json.loads(requests.get(url).content.decode('utf-8'))

    def get_data_list(python_data):
        data_list = python_data['results']
        id_list = []
        for index in range(len(data_list)):
            id_list += [(data_list[index]['id'])]
        return id_list

    def get_nutrition_facts(id):
        apiKey = "0e3889c6bf0c4b98b9e030238f39e8bf"
        url = f"https://api.spoonacular.com/recipes/{str(id)}/nutritionWidget.json?apiKey={apiKey}"
        return json.loads(requests.get(url).content.decode('utf-8'))

    def get_nutrition_list(nutritionFacts):
        calories = float(nutritionFacts['calories'])
        carbs = float(nutritionFacts['carbs'].replace('g', ""))
        fat = float(nutritionFacts['fat'].replace('g', ""))
        protein = float(nutritionFacts['protein'].replace('g', ""))
        return(calories, [carbs, fat, protein])

    def get_recipe_name(id):
        apiKey = "0e3889c6bf0c4b98b9e030238f39e8bf"
        url = f"https://api.spoonacular.com/recipes/{id}/information?includeNutrition=false&apiKey={apiKey}"
        information = json.loads(requests.get(url).content.decode('utf-8'))
        return information['title']

    def plot_pie_chart(title, calories, sizes):
        import matplotlib.pyplot as plt

        labels = 'carbs', 'fat', 'protein'
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        explode = (0, 0, 0)

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')
        plt.title(f"{title} ({calories} kcal)")
        plt.show()

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
        number = 3  # input("How many recipes would you like?: ")

        apiKey = "0e3889c6bf0c4b98b9e030238f39e8bf"
        #url = f"https://api.spoonacular.com/recipes/findByNutrients?minCarbs={minCarbs}&maxCarbs={maxCarbs}&minCalories={minCalories}&maxCalories={maxCalories}&minProteins={minProteins}&maxProteins={maxProteins}&minFats={minFats}&maxFats={maxFats}&number={number}&apiKey={apiKey}"
        url = f"https://api.spoonacular.com/recipes/findByNutrients?minCalories={minCalories}&maxCalories={maxCalories}&number={number}&apiKey={apiKey}"
        options = json.loads(requests.get(url).content.decode('utf-8'))
        options_list = []

        for index in range(len(options)):
            options_list += [(options[index]["id"])]

        return options_list

    ingredient = "potato"  # input("Please enter ingredient: ")
    number = 5  # int(input("Please enter number of searches: "))

    python_data = get_data_string(ingredient, number)
    id_list = get_data_list(python_data)

    for index in range(len(id_list)):
        nutrition_facts = get_nutrition_facts(id_list[index])
        calories, nutrition_list = get_nutrition_list(nutrition_facts)
        title = get_recipe_name(id_list[index])
        plot_pie_chart(title, calories, nutrition_list)

    customized_list = get_customized_recipe_ID_list()
    for index in range(len(customized_list)):
        nutrition_facts = get_nutrition_facts(customized_list[index])
        calories, nutrition_list = get_nutrition_list(nutrition_facts)
        title = get_recipe_name(customized_list[index])
        plot_pie_chart(title, calories, nutrition_list)
    ################################################################################################

    return "Hi, we're done"
