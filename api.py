#Trozo 1
from flask import Flask, render_template
from src import covid_dash, hospitals_tb

#Trozo 2
app = Flask(__name__)
@app.route("/")
def landing_page():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1991, debug=True)

#Trozo 3
@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')
@app.route("/map")
def map():
    return render_template('map.html')