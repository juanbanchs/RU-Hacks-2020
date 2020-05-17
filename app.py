from flask import Flask, render_template
import python_functions as pf
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/test')
def test():
    return render_template('index.html')


@app.route('/')
def index():
    ################################################################################################

    ingredient = "potato"  # input("Please enter ingredient: ")
    number = 1  # int(input("Please enter number of searches: "))

    python_data = pf.get_data_string(ingredient, number)
    id_list = pf.get_data_list(python_data)

    for index in range(len(id_list)):
        nutrition_facts = pf.get_nutrition_facts(id_list[index])
        calories, nutrition_list = pf.get_nutrition_list(nutrition_facts)
        title = pf.get_recipe_name(id_list[index])
        pf.plot_pie_chart(title, calories, nutrition_list)

    customized_list = pf.get_customized_recipe_ID_list()
    for index in range(len(customized_list)):
        nutrition_facts = pf.get_nutrition_facts(customized_list[index])
        calories, nutrition_list = pf.get_nutrition_list(nutrition_facts)
        title = pf.get_recipe_name(customized_list[index])
        pf.plot_pie_chart(title, calories, nutrition_list)
    ################################################################################################

    return "Hi, we're done"
