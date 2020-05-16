from flask import Flask, json
import requests

app = Flask(__name__)


@app.route('/')
def index():

    data = json.loads(requests.get(
        "https://api.spoonacular.com/recipes/search?query=potato&number=2&apiKey=851e31b033fb47518e40cbd5a6b6019a").content.decode('utf-8'))

    # data 2 = json.loads({"results":[{"id":310822,"title":"Potato Cauliflower Parsnip Soup with a Pancetta Potato Hash","readyInMinutes":90,"servings":4,"sourceUrl":"http://www.foodnetwork.com/recipes/nikki-dinki/potato-cauliflower-parsnip-soup-with-a-pancetta-potato-hash-recipe.html","openLicense":0,"image":"potato-cauliflower-parsnip-soup-with-a-pancetta-potato-hash-310822.jpeg"},{"id":202914,"title":"Smoky Sweet Potato Mashed Potato Bake","readyInMinutes":50,"servings":8,"sourceUrl":"http://www.myrecipes.com/recipe/smoky-mashed-sweet-potato-bake-50400000118033/","openLicense":0,"image":"smoky-sweet-potato-mashed-potato-bake-202914.jpg"}],"baseUri":"https://spoonacular.com/recipeImages/","offset":0,"number":2,"totalResults":851,"processingTimeMs":424,"expires":1589872815358,"isStale":false})
    # # potato = "Hi"
    # potato = "hi"
    return data


# if __name__ == "__main__":
# 	app.run(debug=True)

# 	url = "https://api.spoonacular.com/recipes/search?query=potato&number=2&apiKey=851e31b033fb47518e40cbd5a6b6019a"
# 	import requests
#  	import json

# 	return json.loads(requests.get(url).content.decode('utf-8'))
