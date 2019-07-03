import os
import env
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"]  = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route('/', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
    if "username" in session:
        return redirect(session["username"])
    return render_template('login.html')
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('logout.html')

@app.route('/guest')
def guest():
    return render_template('home.html',
    cuisines = mongo.db.cuisines.find().sort('cuisine_type', 1))
    
    
@app.route('/<username>')
def home(username):
    return render_template('home.html',
    cuisines = mongo.db.cuisines.find().sort('cuisine_type', 1))
    
    
@app.route('/add_recipe')
def add_recipe():
    cuisines = mongo.db.cuisines.find()
    return render_template('addrecipe.html', cuisines = cuisines)

@app.route('/manage_recipes')
def manage_recipes():
    return render_template('managerecipes.html',
    recipes = mongo.db.recipes.find({'author.author_username' : session["username"]}))
    
@app.route('/edit_recipe')
def edit_recipe():
    return render_template('editrecipe.html',
    recipes = mongo.db.recipes.find({'author.author_username' : session["username"]}))
    
@app.route('/recipes_for_cuisine/<cuisine_type>')
def recipes_for_cuisine(cuisine_type):
    return render_template('recipesforcuisine.html',
    recipes = mongo.db.recipes.find({'cuisine_type' : cuisine_type}).sort('recipe_name', 1))
    
    
@app.route('/load_recipe/<recipe_name>')
def load_recipe(recipe_name):
    return render_template('viewrecipe.html',
    recipes = mongo.db.recipes.find({'recipe_name' : recipe_name}))


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    num = []
    recipes = mongo.db.recipes
    # recipes.insert_one(request.form.to_dict())
    recipes.insert_one({
        "cuisine_type": request.form.get("cuisine_type"),
        "recipe_name": request.form.get("recipe_name"),
        "img_path": request.form.get("img_path"),
        "recipe_summary": request.form.get("recipe_summary"),
        "recipe_serves": request.form.get("recipe_serves"),
        "preparation_time": request.form.get("preparation_time"),
        "cook_time": request.form.get("cook_time"),
        "allergens": {
            "allergen_1": request.form.get("allergen_1")
        },
        "ingredients": {
            "ingredient1_quantity": request.form.get("ingredient1_quantity"),
            "ingredient1_unit": request.form.get("ingredient1_units"),
            "ingredient1_name": request.form.get("ingredient1_name"),
            "ingredient2_quantity": request.form.get("ingredient2_quantity"),
            "ingredient2_unit": request.form.get("ingredient2_units"),
            "ingredient2_name": request.form.get("ingredient2_name"),
            "ingredient3_quantity": request.form.get("ingredient3_quantity"),
            "ingredient3_unit": request.form.get("ingredient3_units"),
            "ingredient3_name": request.form.get("ingredient3_name"),
            "ingredient4_quantity": request.form.get("ingredient4_quantity"),
            "ingredient4_unit": request.form.get("ingredient4_units"),
            "ingredient4_name": request.form.get("ingredient4_name"),
            "ingredient5_quantity": request.form.get("ingredient5_quantity"),
            "ingredient5_unit": request.form.get("ingredient5_units"),
            "ingredient5_name": request.form.get("ingredient5_name"),
            "ingredient6_quantity": request.form.get("ingredient6_quantity"),
            "ingredient6_unit": request.form.get("ingredient6_units"),
            "ingredient6_name": request.form.get("ingredient6_name"),
            "ingredient7_quantity": request.form.get("ingredient7_quantity"),
            "ingredient7_unit": request.form.get("ingredient7_units"),
            "ingredient7_name": request.form.get("ingredient7_name"),
            "ingredient8_quantity": request.form.get("ingredient8_quantity"),
            "ingredient8_unit": request.form.get("ingredient8_units"),
            "ingredient8_name": request.form.get("ingredient8_name"),
            "ingredient9_quantity": request.form.get("ingredient9_quantity"),
            "ingredient9_unit": request.form.get("ingredient9_units"),
            "ingredient9_name": request.form.get("ingredient9_name"),
            "ingredient10_quantity": request.form.get("ingredient10_quantity"),
            "ingredient10_unit": request.form.get("ingredient10_units"),
            "ingredient10_name": request.form.get("ingredient10_name")
        },
        "methods": {
            "method_step1": request.form.get("method_step1"),
            "method_step2": request.form.get("method_step2"),
            "method_step3": request.form.get("method_step3"),
            "method_step4": request.form.get("method_step4"),
            "method_step5": request.form.get("method_step5"),
            "method_step6": request.form.get("method_step6"),
            "method_step7": request.form.get("method_step7"),
            "method_step8": request.form.get("method_step8"),
            "method_step9": request.form.get("method_step9"),
            "method_step10": request.form.get("method_step10")
        },
        "author": {
            "author_username": request.form.get("author_username"),
            "author_region": request.form.get("author_region")
        },
        "public_visibility": request.form.get("public_visibility")
    })
    return redirect(url_for('manage_recipes'))

@app.route('/index_of_recipes')
def index_of_recipes():
    return render_template('indexofrecipes.html',
    recipes = mongo.db.recipes.find().sort('recipe_name', 1))

if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
        port = int(os.environ.get('PORT')),
        debug = True)