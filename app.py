import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"]  = 'online-cookbook'
app.config["MONGO_URI"] = 'mongodb://admin:u537a6m1n@ds213665.mlab.com:13665/online-cookbook'

mongo = PyMongo(app)

@app.route('/')
@app.route('/load_recipes')
def load_recipes():
    return render_template("recipes.html",
    recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)