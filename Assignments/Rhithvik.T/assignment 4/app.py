from flask import Flask,render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')





if(__name__ == "__main__"):
   port = os.environ.get("PORT",5000)
   app.run(port=port,host='0.0.0.0',debug=True)