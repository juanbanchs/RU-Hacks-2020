import requests
import json
import matplotlib.pyplot as plt


def get_data_string(ingredient, number):
    apiKey = "851e31b033fb47518e40cbd5a6b6019a"
    url = f"https://api.spoonacular.com/recipes/search?query={ingredient}&number={number}&apiKey={apiKey}"

    return json.loads(requests.get(url).content.decode('utf-8'))


def get_data_list(python_data):
    data_list = python_data['results']
    id_list = []
    for index in range(len(data_list)):
        id_list += [(data_list[index]['id'])]
    return id_list


def get_nutrition_facts(id):
    apiKey = "851e31b033fb47518e40cbd5a6b6019a"
    url = f"https://api.spoonacular.com/recipes/{str(id)}/nutritionWidget.json?apiKey={apiKey}"
    return json.loads(requests.get(url).content.decode('utf-8'))


def get_nutrition_list(nutritionFacts):
    calories = float(nutritionFacts['calories'])
    carbs = float(nutritionFacts['carbs'].replace('g', ""))
    fat = float(nutritionFacts['fat'].replace('g', ""))
    protein = float(nutritionFacts['protein'].replace('g', ""))
    return(calories, [carbs, fat, protein])


def get_recipe_name(id):
    apiKey = "851e31b033fb47518e40cbd5a6b6019a"
    url = f"https://api.spoonacular.com/recipes/{id}/information?includeNutrition=false&apiKey={apiKey}"
    information = json.loads(requests.get(url).content.decode('utf-8'))
    return information['title']


def plot_pie_chart(title, calories, sizes):
    labels = 'carbs', 'fat', 'protein'
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0, 0, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.title(f"{title} ({calories} kcal)")
    plt.show()


def get_customized_recipe_ID_list():
    # minCarbs = input("Please enter minimum carbs (if none, enter 0): ")
    # maxCarbs = input("Please enter maximum carbs (if none, enter 0): ")
    # input("Please enter minimum calories (if none, enter 0): ")
    minCalories = 100
    # input("Please enter maximum calories (if none, enter 0): ")
    maxCalories = 460
    # minProteins = input("Please enter minimum proteins (if none, enter 0): ")
    # maxProteins = input("Please enter maximum proteins (if none, enter 0): ")
    # minFats = input("Please enter minimum fats (if none, enter 0): ")
    # maxFats = input("Please enter maximum fats (if none, enter 0): ")
    number = 1  # input("How many recipes would you like?: ")

    apiKey = "851e31b033fb47518e40cbd5a6b6019a"
    # url = f"https://api.spoonacular.com/recipes/findByNutrients?minCarbs={minCarbs}&maxCarbs={maxCarbs}&minCalories={minCalories}&maxCalories={maxCalories}&minProteins={minProteins}&maxProteins={maxProteins}&minFats={minFats}&maxFats={maxFats}&number={number}&apiKey={apiKey}"
    url = f"https://api.spoonacular.com/recipes/findByNutrients?minCalories={minCalories}&maxCalories={maxCalories}&number={number}&apiKey={apiKey}"
    options = json.loads(requests.get(url).content.decode('utf-8'))
    options_list = []

    for index in range(len(options)):
        options_list += [(options[index]["id"])]

    return options_list
