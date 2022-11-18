from flask import Flask, render_template, requests
from newsapi import NewsApiClient

# init flask app
app = Flask(__name__)

# Init news api
newsapi = NewsApiClient(api_key='73ebcf7998bd494c9ae7ef215cdb11fd')


@app.route("/")
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=73ebcf7998bd494c9ae7ef215cdb11f"
    r = request.get(url).json

    cases = {
         'articles' :r['articles']
     }

     return render_template("index.html", case = cases)
if __name__ == "__main__":
	app.run(debug = True)
