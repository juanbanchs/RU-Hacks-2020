import io
import random
from flask import Flask, Response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure

from flask import Flask, render_template, send_file, Response
import python_functions as pf
from flask_bootstrap import Bootstrap
import matplotlib.pyplot as plt

app = Flask(__name__)
Bootstrap(app)


@app.route("/test")
def test():
    """ Returns html with the img tag for your plot.
    """
    num_x_points = int(request.args.get("num_x_points", 50))
    # in a real app you probably want to use a flask template.
    return render_template("index.html", num_x_points=num_x_points)


@app.route("/matplot-as-image-<int:num_x_points>.svg")
def plot_svg(num_x_points=50):
    """ renders the plot on the fly.
    """
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_points = range(num_x_points)
    axis.plot(x_points, [random.randint(1, 30) for x in x_points])

    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")


# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/plot.png')
# def plot_png():

#     ingredient = "potato"  # input("Please enter ingredient: ")
#     number = 1  # int(input("Please enter number of searches: "))

#     python_data = pf.get_data_string(ingredient, number)
#     id_list = pf.get_data_list(python_data)

#     for index in range(len(id_list)):
#         nutrition_facts = pf.get_nutrition_facts(id_list[index])
#         calories, nutrition_list = pf.get_nutrition_list(nutrition_facts)
#         title = pf.get_recipe_name(id_list[index])
#         # pf.plot_pie_chart(title, calories, nutrition_list)

#     customized_list = pf.get_customized_recipe_ID_list()
#     for index in range(len(customized_list)):
#         nutrition_facts = pf.get_nutrition_facts(customized_list[index])
#         calories, nutrition_list = pf.get_nutrition_list(nutrition_facts)
#         title = pf.get_recipe_name(customized_list[index])
#         fig = pf.plot_pie_chart(title, calories, nutrition_list)

#     return Response(fig, mimetype="image/png")
#     # "<img src='/plot.png' alt='my plot'>"

# #   <img src="/plot.png" alt="my plot">
# #  Dynamic routings /id /something if I want to do moultiple

# # @app.route('/plot.png')
# # def plot_png():
# #   generate_image_here()
# #   return Response(image, mimetype='image/png')
# # <img src="/plot.png" alt="my plot">
# # http://www.compjour.org/lessons/flask-single-page/multiple-dynamic-routes-in-flask/
# # def plot_png(name):
# # $done


# @app.route('/background_process_test')
# def background_process_test():

#     ################################################################################################

#     ingredient = "potato"  # input("Please enter ingredient: ")
#     number = 1  # int(input("Please enter number of searches: "))

#     python_data = pf.get_data_string(ingredient, number)
#     id_list = pf.get_data_list(python_data)

#     for index in range(len(id_list)):
#         nutrition_facts = pf.get_nutrition_facts(id_list[index])
#         calories, nutrition_list = pf.get_nutrition_list(nutrition_facts)
#         title = pf.get_recipe_name(id_list[index])
#         pf.plot_pie_chart(title, calories, nutrition_list)

#     customized_list = pf.get_customized_recipe_ID_list()
#     for index in range(len(customized_list)):
#         nutrition_facts = pf.get_nutrition_facts(customized_list[index])
#         calories, nutrition_list = pf.get_nutrition_list(nutrition_facts)
#         title = pf.get_recipe_name(customized_list[index])
#         pf.plot_pie_chart(title, calories, nutrition_list)
#     ################################################################################################

#     return render_template('index.html')
