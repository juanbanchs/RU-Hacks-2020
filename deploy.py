from flask import Flask, requests, json

app = Flask(__name__)

@app.route('/')
def index():
	
	url = "https://api.spoonacular.com/recipes/search?query=potato&number=2&apiKey=851e31b033fb47518e40cbd5a6b6019a"
	import requests
 	import json
  
	return json.loads(requests.get(url).content.decode('utf-8'))


# if __name__ == "__main__":
# 	app.run(debug=True)