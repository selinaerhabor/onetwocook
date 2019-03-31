import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"]  = 'online-cookbook'
app.config["MONGO_URI"] = 'mongodb://admin:u537a6m1n@ds213665.mlab.com:13665/online-cookbook'

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('cuisines.html',
    cuisines=mongo.db.cuisines.find().sort('cuisine_type', 1))

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html')

@app.route('/manage_recipes')
def manage_recipes():
    return render_template('managerecipes.html')
    
@app.route('/edit_recipe')
def edit_recipe():
    return render_template('editrecipe.html')
    
@app.route('/recipes_for_cuisine/<cuisine_type>')
def recipes_for_cuisine(cuisine_type):
    return render_template('recipesforcuisine.html',
    recipes=mongo.db.recipes.find({'cuisine_type': cuisine_type}).sort('recipe_name', 1))
    
    
@app.route('/load_recipe/<recipe_name>')
def load_recipe(recipe_name):
    return render_template('viewrecipe.html',
    recipes=mongo.db.recipes.find({'recipe_name': recipe_name}))


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('home'))

@app.route('/index_of_recipes')
def index_of_recipes():
    return render_template('indexofrecipes.html',
    recipes=mongo.db.recipes.find().sort('recipe_name', 1))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)