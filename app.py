import os
import env
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

### Flask
app = Flask(__name__)

### Environment Variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"]  = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

### Mongo
mongo = PyMongo(app)

### Application Login
@app.route('/', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
    if "username" in session:
        return redirect(session["username"])
    return render_template('login.html')

### Logout Page
@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('logout.html')

### Welcome Page - Guest View
@app.route('/guest')
def guest():
    return render_template('home.html',
    cuisines = mongo.db.cuisines.find().sort('cuisine_type', 1))

### Welcome Page - Username
@app.route('/<username>')
def home(username):
    return render_template('home.html',
    cuisines = mongo.db.cuisines.find().sort('cuisine_type', 1))
    
### 'Add a Recipe' Page
@app.route('/add_recipe')
def add_recipe():
    cuisines = mongo.db.cuisines.find().sort('cuisine_type', 1)
    return render_template('addrecipe.html', cuisines = cuisines)

### 'Add a Cuisine' Page
@app.route('/add_cuisine')
def add_cuisine():
    return render_template('addcuisine.html')
    
### Submission of 'Add a Cuisine' Form to mLab Database
@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    new_cuisines = mongo.db.cuisines
    new_cuisines.insert_one({
        "cuisine_type": request.form.get("cuisine_type"),
        "cuisine_summary": request.form.get("cuisine_summary"),
        "author_username": session['username']
    })
    return redirect(url_for('add_recipe'))
    
### 'Manage Your Recipes' Page
@app.route('/manage_recipes')
def manage_recipes():
    return render_template('managerecipes.html',
        ### 'Manage Your Recipes' Section
        user_recipes = mongo.db.recipes.find({'author.author_username' : session["username"]}),
        ### 'Manage Your Cuisines' Section
        user_cuisines = mongo.db.cuisines.find({'author_username' : session["username"]}),
        ### Recipe count for user
        user_recipe_count = mongo.db.recipes.find({'author.author_username' : session["username"]}).count(),
        ### Cuisine count for user
        user_cuisine_count = mongo.db.cuisines.find({'author_username' : session["username"]}).count()
    )
    
### 'Edit Recipe' Page (via 'Manage Your Recipes')
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe_selected =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipes=recipe_selected)
    
### 'Edit Cuisine' Page (via 'Manage Your Recipes' Secondary tab - 'Manage Your Cuisines')
@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    cuisine_selected =  mongo.db.cuisines.find_one({'_id': ObjectId(cuisine_id)})
    return render_template('editcuisine.html', cuisines=cuisine_selected)
    
### List of all recipes under selected Cuisine Type
@app.route('/recipes_for_cuisine/<cuisine_type>')
def recipes_for_cuisine(cuisine_type):
    return render_template('recipesforcuisine.html',
    recipes = mongo.db.recipes.find({"cuisine_type" : cuisine_type, "public_visibility" : "yes"}).sort('recipe_name', 1))
    
### View Recipe Page
@app.route('/load_recipe/<recipe_name>')
def load_recipe(recipe_name):
    return render_template('viewrecipe.html',
    recipes = mongo.db.recipes.find({'recipe_name' : recipe_name}))

### Submission of 'Add a Recipe' Form to mLab Database
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one({
        "cuisine_type": request.form.get("cuisine_type"),
        "recipe_name": request.form.get("recipe_name"),
        "img_path": request.form.get("img_path"),
        "recipe_summary": request.form.get("recipe_summary"),
        "recipe_serves": request.form.get("recipe_serves"),
        "preparation_time": request.form.get("preparation_time"),
        "pt_time_units": request.form.get("pt_time_units"),
        "cook_time": request.form.get("cook_time"),
        "ct_time_units": request.form.get("ct_time_units"),
        "allergens": request.form.getlist("allergens"),
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
            "ingredient10_name": request.form.get("ingredient10_name"),
            "ingredient11_quantity": request.form.get("ingredient11_quantity"),
            "ingredient11_unit": request.form.get("ingredient11_units"),
            "ingredient11_name": request.form.get("ingredient11_name"),
            "ingredient12_quantity": request.form.get("ingredient12_quantity"),
            "ingredient12_unit": request.form.get("ingredient12_units"),
            "ingredient12_name": request.form.get("ingredient12_name"),
            "ingredient13_quantity": request.form.get("ingredient13_quantity"),
            "ingredient13_unit": request.form.get("ingredient13_units"),
            "ingredient13_name": request.form.get("ingredient13_name"),
            "ingredient14_quantity": request.form.get("ingredient14_quantity"),
            "ingredient14_unit": request.form.get("ingredient14_units"),
            "ingredient14_name": request.form.get("ingredient14_name"),
            "ingredient15_quantity": request.form.get("ingredient15_quantity"),
            "ingredient15_unit": request.form.get("ingredient15_units"),
            "ingredient15_name": request.form.get("ingredient15_name"),
            "ingredient16_quantity": request.form.get("ingredient16_quantity"),
            "ingredient16_unit": request.form.get("ingredient16_units"),
            "ingredient16_name": request.form.get("ingredient16_name"),
            "ingredient17_quantity": request.form.get("ingredient17_quantity"),
            "ingredient17_unit": request.form.get("ingredient17_units"),
            "ingredient17_name": request.form.get("ingredient17_name"),
            "ingredient18_quantity": request.form.get("ingredient18_quantity"),
            "ingredient18_unit": request.form.get("ingredient18_units"),
            "ingredient18_name": request.form.get("ingredient18_name"),
            "ingredient19_quantity": request.form.get("ingredient19_quantity"),
            "ingredient19_unit": request.form.get("ingredient19_units"),
            "ingredient19_name": request.form.get("ingredient19_name"),
            "ingredient20_quantity": request.form.get("ingredient20_quantity"),
            "ingredient20_unit": request.form.get("ingredient20_units"),
            "ingredient20_name": request.form.get("ingredient20_name")
        },
        "method": {
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
            "author_username": session['username'],
            "author_region": request.form.get("author_region")
        },
        "public_visibility": request.form.get("public_visibility")
    })
    return redirect(url_for('add_recipe'))
    
### Moves recipes to 'Liked Recipe' section (under 'Manage Your Recipes' page)
@app.route('/liked_recipe/<recipe_id>')
def like_recipe(recipe_id):
    mongo.db.recipes.save({'_id': ObjectId(recipe_id)})
    return redirect(url_for('manage_recipes'))

### Update recipes in mLab database
@app.route('/update_recipe/<recipe_id>', methods=['POST'])    
def update_recipe(recipe_id):
    mongo.db.recipes.update(
        {'_id': ObjectId(recipe_id)},
        {
        "cuisine_type": request.form.get("cuisine_type"),
        "recipe_name": request.form.get("recipe_name"),
        "img_path": request.form.get("img_path"),
        "recipe_summary": request.form.get("recipe_summary"),
        "recipe_serves": request.form.get("recipe_serves"),
        "preparation_time": request.form.get("preparation_time"),
        "pt_time_units": request.form.get("pt_time_units"),
        "cook_time": request.form.get("cook_time"),
        "ct_time_units": request.form.get("ct_time_units"),
        "allergens": request.form.getlist("allergens"),
        "gluten-free": request.form.get("gluten-free"),
        "vegetarian": request.form.get("vegetarian"),
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
            "ingredient10_name": request.form.get("ingredient10_name"),
            "ingredient11_quantity": request.form.get("ingredient11_quantity"),
            "ingredient11_unit": request.form.get("ingredient11_units"),
            "ingredient11_name": request.form.get("ingredient11_name"),
            "ingredient12_quantity": request.form.get("ingredient12_quantity"),
            "ingredient12_unit": request.form.get("ingredient12_units"),
            "ingredient12_name": request.form.get("ingredient12_name"),
            "ingredient13_quantity": request.form.get("ingredient13_quantity"),
            "ingredient13_unit": request.form.get("ingredient13_units"),
            "ingredient13_name": request.form.get("ingredient13_name"),
            "ingredient14_quantity": request.form.get("ingredient14_quantity"),
            "ingredient14_unit": request.form.get("ingredient14_units"),
            "ingredient14_name": request.form.get("ingredient14_name"),
            "ingredient15_quantity": request.form.get("ingredient15_quantity"),
            "ingredient15_unit": request.form.get("ingredient15_units"),
            "ingredient15_name": request.form.get("ingredient15_name"),
            "ingredient16_quantity": request.form.get("ingredient16_quantity"),
            "ingredient16_unit": request.form.get("ingredient16_units"),
            "ingredient16_name": request.form.get("ingredient16_name"),
            "ingredient17_quantity": request.form.get("ingredient17_quantity"),
            "ingredient17_unit": request.form.get("ingredient17_units"),
            "ingredient17_name": request.form.get("ingredient17_name"),
            "ingredient18_quantity": request.form.get("ingredient18_quantity"),
            "ingredient18_unit": request.form.get("ingredient18_units"),
            "ingredient18_name": request.form.get("ingredient18_name"),
            "ingredient19_quantity": request.form.get("ingredient19_quantity"),
            "ingredient19_unit": request.form.get("ingredient19_units"),
            "ingredient19_name": request.form.get("ingredient19_name"),
            "ingredient20_quantity": request.form.get("ingredient20_quantity"),
            "ingredient20_unit": request.form.get("ingredient20_units"),
            "ingredient20_name": request.form.get("ingredient20_name")
        },
        "method": {
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
            "author_username": session['username'],
            "author_region": request.form.get("author_region")
        },
        "public_visibility": request.form.get("public_visibility")
    })
    return redirect(url_for('manage_recipes'))

### Update recipes in mLab database
@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])    
def update_cuisine(cuisine_id):
    mongo.db.cuisines.update(
        {'_id': ObjectId(cuisine_id)},
        {"cuisine_type": request.form.get("cuisine_type"),
        "cuisine_summary": request.form.get("cuisine_summary")}
    )
        
### Index of Recipes
@app.route('/index_of_recipes')
def index_of_recipes():
    return render_template('indexofrecipes.html',
    recipes = mongo.db.recipes.find().sort('recipe_name', 1))

### Delete created Cuisine Type
@app.route('/delete_cuisine/<cuisine_id>', methods=['POST'])
def delete_cuisine(cuisine_id):
    mongo.db.cuisines.remove({'_id': ObjectId(cuisine_id)})
    return redirect(url_for('manage_recipes'))
    
### Delete a Recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('manage_recipes'))

if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
        port = int(os.environ.get('PORT')),
        debug = True)