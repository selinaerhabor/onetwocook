import os
import env
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from jinja2 import Template

# Flask
app = Flask(__name__)

# Configuration Variables
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MONGO_DBNAME']  = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

# Mongo
mongo = PyMongo(app)

# Application Login
@app.route('/', methods = ['GET', 'POST'])
def login():
    page_title = 'Login | OneTwoCook'
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['user_dob'] = request.form['user_dob']
        session['user_region'] = request.form['user_region']
    if 'username' in session:
        return redirect(url_for('home'))
    return render_template('login.html', page_title = page_title)

# Logout Page
@app.route('/logout')
def logout():
    page_title = 'Logout | OneTwoCook'
    session.pop('username', None)
    return render_template('logout.html', page_title = page_title)

# Welcome Page - Guest View
@app.route('/guest')
def guest():
    page_title = 'Home | OneTwoCook'
    cuisines = mongo.db.cuisines.find().sort('cuisine_type', 1)
    return render_template('home.html', cuisines = cuisines, page_title = page_title)

# Welcome Page - Users who created username
@app.route('/home')
def home():
    page_title = 'Home | OneTwoCook'
    cuisines = mongo.db.cuisines.find().sort('cuisine_type', 1)
    return render_template('home.html', cuisines = cuisines, page_title = page_title)
    
# 'Add a Recipe' Page
@app.route('/add_recipe')
def add_recipe():
    page_title = 'Add Recipe | OneTwoCook'
    cuisines = mongo.db.cuisines.find().sort('cuisine_type', 1)
    return render_template('addrecipe.html', cuisines = cuisines, page_title = page_title)

# 'Add a Cuisine' Page
@app.route('/add_cuisine')
def add_cuisine():
    page_title = 'Add Cuisine | OneTwoCook'
    return render_template('addcuisine.html', page_title = page_title)

"""  
Checks if a cuisine with the same name already exists and if so prompts user to 
create a different cuisine type. Only unique cuisine types will be submitted to 
MongoDB mLab Database.
"""
@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisines = mongo.db.cuisines.find_one({ 
        "cuisine_type": 
            {"$regex": request.form.get('cuisine_type'),
            "$options":"i"}
        })
    if cuisines:
        alert = "*The cuisine type you entered already exists. Please choose another cuisine.*"
        return render_template('addcuisine.html', alert = alert, cuisines = cuisines)
    else:
        mongo.db.cuisines.insert_one({
            'cuisine_type': request.form.get('cuisine_type'),
            'cuisine_summary': request.form.get('cuisine_summary'),
            'author_username': session['username'],
            'author_dob': session['user_dob'],
            'author_region': session['user_region']
        })
    return redirect(url_for('add_recipe'))
    
# 'Manage Your Recipes' Page
@app.route('/manage_creations')
def manage_creations():
    page_title = 'Manage Your Recipes | OneTwoCook'
    # 'Manage Your Recipes' Section
    user_recipes = mongo.db.recipes.find({
        'author.author_username' : session['username'], 
        'author.author_region' : session['user_region'], 
        'author.author_dob' : session['user_dob']}).sort('recipe_name', 1)
    # 'Manage Your Cuisines' Section
    user_cuisines = mongo.db.cuisines.find({
        'author_username' : session['username'], 
        'author_region' : session['user_region'], 
        'author_dob' : session['user_dob']}).sort('cuisine_type', 1)
    # Recipe count for user
    user_recipe_count = mongo.db.recipes.find({
        'author.author_username' : session['username'], 
        'author.author_region' : session['user_region'], 
        'author.author_dob' : session['user_dob']}).count()
    # Cuisine count for user
    user_cuisine_count = mongo.db.cuisines.find({
        'author_username' : session['username'], 
        'author_region' : session['user_region'], 
        'author_dob' : session['user_dob']}).count()
    return render_template('manageyourcreations.html', 
    recipes = user_recipes, 
    cuisines = user_cuisines, 
    user_recipe_count = user_recipe_count, 
    user_cuisine_count = user_cuisine_count,
    page_title = page_title)
    
# 'Edit Recipe' Page (via 'Manage Your Creations')
@app.route('/edit_recipe/<recipe_name>/<recipe_id>')
def edit_recipe(recipe_name, recipe_id):
    page_title = 'Edit ' + recipe_name + ' | OneTwoCook'
    units = mongo.db.units.find().sort('ingredient_units', 1)
    cuisines = mongo.db.cuisines.find().sort('cuisine_type', 1)
    recipe_selected =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id), 'recipe_name': recipe_name})
    return render_template('editrecipe.html', recipes = recipe_selected, cuisines = cuisines, units = units, page_title = page_title)
    
# 'Edit Cuisine' Page (via 'Manage Your Creations' Secondary tab - 'Manage Your Creations')
@app.route('/edit_cuisine/<cuisine_type>/<cuisine_id>')
def edit_cuisine(cuisine_type, cuisine_id):
    page_title = 'Edit ' + cuisine_type + ' | OneTwoCook'
    cuisine_selected =  mongo.db.cuisines.find_one({'_id': ObjectId(cuisine_id), 'cuisine_type': cuisine_type })
    return render_template('editcuisine.html', cuisines = cuisine_selected, page_title = page_title)
    
# List of all recipes under selected Cuisine Type
@app.route('/recipes_for_cuisine/<cuisine_type>')
def recipes_for_cuisine(cuisine_type):
    page_title = cuisine_type + ' Recipes | OneTwoCook'
    cuisines = mongo.db.cuisines.find().sort('cuisine_type', 1)
    public_recipes = mongo.db.recipes.find({'cuisine_type' : cuisine_type, 'public_visibility' : 'on'}).sort('recipe_name', 1)
    heading = cuisine_type + ' Recipes'
    return render_template('recipesforcuisine.html', recipes = public_recipes, cuisines = cuisines, heading = heading, page_title = page_title)
    
# View Recipe Page (Recipes where public_visibility = 'on')
@app.route('/view_recipe/<recipe_name>/<recipe_id>/')
def view_recipe(recipe_name, recipe_id):
    recipes = mongo.db.recipes.find({'_id': ObjectId(recipe_id), 'recipe_name': recipe_name})
    page_title = recipe_name + ' | OneTwoCook'
    cuisines = mongo.db.cuisines.find()
    previous_url = 'recipes_for_cuisine'
    return render_template('viewrecipe.html', recipes = recipes,
    cuisines = cuisines, previous_url = previous_url, 
    page_title = page_title)
    
# View Your Recipe Page (via Manage Your Recipes)
@app.route('/view_your_recipe/<recipe_name>/<recipe_id>')
def view_your_recipe(recipe_name, recipe_id):
    page_title = recipe_name + ' | OneTwoCook'
    view_your_recipe = mongo.db.recipes.find({'_id': ObjectId(recipe_id), 'recipe_name': recipe_name})
    previous_url = url_for('manage_creations')
    previous_page = 'Manage Your Creations'
    return render_template('viewrecipe.html', recipes = view_your_recipe, 
    previous_url = previous_url, previous_page = previous_page, page_title = page_title)

# Submission of 'Add a Recipe' Form to mLab Database
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    mongo.db.recipes.insert_one({
        'cuisine_type': request.form.get('cuisine_type'),
        'recipe_name': request.form.get('recipe_name'),
        'img_path': request.form.get('img_path'),
        'recipe_summary': request.form.get('recipe_summary'),
        'recipe_serves': request.form.get('recipe_serves'),
        'preparation_time': request.form.get('preparation_time'),
        'pt_units': request.form.get('pt_units'),
        'cook_time': request.form.get('cook_time'),
        'ct_units': request.form.get('ct_units'),
        'allergens': request.form.get('allergens'),
        'gluten_free': request.form.get('gluten_free'),
        'vegetarian': request.form.get('vegetarian'),
        'ingredients': {
            'ingredient1_quantity': request.form.get('ingredient1_quantity'),
            'ingredient1_units': request.form.get('ingredient1_units'),
            'ingredient1_name': request.form.get('ingredient1_name'),
            'ingredient2_quantity': request.form.get('ingredient2_quantity'),
            'ingredient2_units': request.form.get('ingredient2_units'),
            'ingredient2_name': request.form.get('ingredient2_name'),
            'ingredient3_quantity': request.form.get('ingredient3_quantity'),
            'ingredient3_units': request.form.get('ingredient3_units'),
            'ingredient3_name': request.form.get('ingredient3_name'),
            'ingredient4_quantity': request.form.get('ingredient4_quantity'),
            'ingredient4_units': request.form.get('ingredient4_units'),
            'ingredient4_name': request.form.get('ingredient4_name'),
            'ingredient5_quantity': request.form.get('ingredient5_quantity'),
            'ingredient5_units': request.form.get('ingredient5_units'),
            'ingredient5_name': request.form.get('ingredient5_name'),
            'ingredient6_quantity': request.form.get('ingredient6_quantity'),
            'ingredient6_units': request.form.get('ingredient6_units'),
            'ingredient6_name': request.form.get('ingredient6_name'),
            'ingredient7_quantity': request.form.get('ingredient7_quantity'),
            'ingredient7_units': request.form.get('ingredient7_units'),
            'ingredient7_name': request.form.get('ingredient7_name'),
            'ingredient8_quantity': request.form.get('ingredient8_quantity'),
            'ingredient8_units': request.form.get('ingredient8_units'),
            'ingredient8_name': request.form.get('ingredient8_name'),
            'ingredient9_quantity': request.form.get('ingredient9_quantity'),
            'ingredient9_units': request.form.get('ingredient9_units'),
            'ingredient9_name': request.form.get('ingredient9_name'),
            'ingredient10_quantity': request.form.get('ingredient10_quantity'),
            'ingredient10_units': request.form.get('ingredient10_units'),
            'ingredient10_name': request.form.get('ingredient10_name'),
            'ingredient11_quantity': request.form.get('ingredient11_quantity'),
            'ingredient11_units': request.form.get('ingredient11_units'),
            'ingredient11_name': request.form.get('ingredient11_name'),
            'ingredient12_quantity': request.form.get('ingredient12_quantity'),
            'ingredient12_units': request.form.get('ingredient12_units'),
            'ingredient12_name': request.form.get('ingredient12_name'),
            'ingredient13_quantity': request.form.get('ingredient13_quantity'),
            'ingredient13_units': request.form.get('ingredient13_units'),
            'ingredient13_name': request.form.get('ingredient13_name'),
            'ingredient14_quantity': request.form.get('ingredient14_quantity'),
            'ingredient14_units': request.form.get('ingredient14_units'),
            'ingredient14_name': request.form.get('ingredient14_name'),
            'ingredient15_quantity': request.form.get('ingredient15_quantity'),
            'ingredient15_units': request.form.get('ingredient15_units'),
            'ingredient15_name': request.form.get('ingredient15_name'),
            'ingredient16_quantity': request.form.get('ingredient16_quantity'),
            'ingredient16_units': request.form.get('ingredient16_units'),
            'ingredient16_name': request.form.get('ingredient16_name'),
            'ingredient17_quantity': request.form.get('ingredient17_quantity'),
            'ingredient17_units': request.form.get('ingredient17_units'),
            'ingredient17_name': request.form.get('ingredient17_name'),
            'ingredient18_quantity': request.form.get('ingredient18_quantity'),
            'ingredient18_units': request.form.get('ingredient18_units'),
            'ingredient18_name': request.form.get('ingredient18_name'),
            'ingredient19_quantity': request.form.get('ingredient19_quantity'),
            'ingredient19_units': request.form.get('ingredient19_units'),
            'ingredient19_name': request.form.get('ingredient19_name'),
            'ingredient20_quantity': request.form.get('ingredient20_quantity'),
            'ingredient20_units': request.form.get('ingredient20_units'),
            'ingredient20_name': request.form.get('ingredient20_name')
        },
        'method': {
            'method_step1': request.form.get('method_step1'),
            'method_step2': request.form.get('method_step2'),
            'method_step3': request.form.get('method_step3'),
            'method_step4': request.form.get('method_step4'),
            'method_step5': request.form.get('method_step5'),
            'method_step6': request.form.get('method_step6'),
            'method_step7': request.form.get('method_step7'),
            'method_step8': request.form.get('method_step8'),
            'method_step9': request.form.get('method_step9'),
            'method_step10': request.form.get('method_step10')
        },
        'author': {
            'author_username': session['username'],
            'author_dob': session['user_dob'],
            'author_region': session['user_region']
        },
        'public_visibility': request.form.get('public_visibility')
    })
    return redirect(url_for('manage_creations'))

### Update recipes in mLab database
@app.route('/update_recipe/<recipe_id>', methods=['POST'])    
def update_recipe(recipe_id):
    mongo.db.recipes.update(
        {'_id': ObjectId(recipe_id)},
        {
        'cuisine_type': request.form.get('cuisine_type'),
        'recipe_name': request.form.get('recipe_name'),
        'img_path': request.form.get('img_path'),
        'recipe_summary': request.form.get('recipe_summary'),
        'recipe_serves': request.form.get('recipe_serves'),
        'preparation_time': request.form.get('preparation_time'),
        'pt_units': request.form.get('pt_units'),
        'cook_time': request.form.get('cook_time'),
        'ct_units': request.form.get('ct_units'),
        'allergens': request.form.get('allergens'),
        'gluten_free': request.form.get('gluten_free'),
        'vegetarian': request.form.get('vegetarian'),
        'ingredients': {
            'ingredient1_quantity': request.form.get('ingredient1_quantity'),
            'ingredient1_units': request.form.get('ingredient1_units'),
            'ingredient1_name': request.form.get('ingredient1_name'),
            'ingredient2_quantity': request.form.get('ingredient2_quantity'),
            'ingredient2_units': request.form.get('ingredient2_units'),
            'ingredient2_name': request.form.get('ingredient2_name'),
            'ingredient3_quantity': request.form.get('ingredient3_quantity'),
            'ingredient3_units': request.form.get('ingredient3_units'),
            'ingredient3_name': request.form.get('ingredient3_name'),
            'ingredient4_quantity': request.form.get('ingredient4_quantity'),
            'ingredient4_units': request.form.get('ingredient4_units'),
            'ingredient4_name': request.form.get('ingredient4_name'),
            'ingredient5_quantity': request.form.get('ingredient5_quantity'),
            'ingredient5_units': request.form.get('ingredient5_units'),
            'ingredient5_name': request.form.get('ingredient5_name'),
            'ingredient6_quantity': request.form.get('ingredient6_quantity'),
            'ingredient6_units': request.form.get('ingredient6_units'),
            'ingredient6_name': request.form.get('ingredient6_name'),
            'ingredient7_quantity': request.form.get('ingredient7_quantity'),
            'ingredient7_units': request.form.get('ingredient7_units'),
            'ingredient7_name': request.form.get('ingredient7_name'),
            'ingredient8_quantity': request.form.get('ingredient8_quantity'),
            'ingredient8_units': request.form.get('ingredient8_units'),
            'ingredient8_name': request.form.get('ingredient8_name'),
            'ingredient9_quantity': request.form.get('ingredient9_quantity'),
            'ingredient9_units': request.form.get('ingredient9_units'),
            'ingredient9_name': request.form.get('ingredient9_name'),
            'ingredient10_quantity': request.form.get('ingredient10_quantity'),
            'ingredient10_units': request.form.get('ingredient10_units'),
            'ingredient10_name': request.form.get('ingredient10_name'),
            'ingredient11_quantity': request.form.get('ingredient11_quantity'),
            'ingredient11_units': request.form.get('ingredient11_units'),
            'ingredient11_name': request.form.get('ingredient11_name'),
            'ingredient12_quantity': request.form.get('ingredient12_quantity'),
            'ingredient12_units': request.form.get('ingredient12_units'),
            'ingredient12_name': request.form.get('ingredient12_name'),
            'ingredient13_quantity': request.form.get('ingredient13_quantity'),
            'ingredient13_units': request.form.get('ingredient13_units'),
            'ingredient13_name': request.form.get('ingredient13_name'),
            'ingredient14_quantity': request.form.get('ingredient14_quantity'),
            'ingredient14_units': request.form.get('ingredient14_units'),
            'ingredient14_name': request.form.get('ingredient14_name'),
            'ingredient15_quantity': request.form.get('ingredient15_quantity'),
            'ingredient15_units': request.form.get('ingredient15_units'),
            'ingredient15_name': request.form.get('ingredient15_name'),
            'ingredient16_quantity': request.form.get('ingredient16_quantity'),
            'ingredient16_units': request.form.get('ingredient16_units'),
            'ingredient16_name': request.form.get('ingredient16_name'),
            'ingredient17_quantity': request.form.get('ingredient17_quantity'),
            'ingredient17_units': request.form.get('ingredient17_units'),
            'ingredient17_name': request.form.get('ingredient17_name'),
            'ingredient18_quantity': request.form.get('ingredient18_quantity'),
            'ingredient18_units': request.form.get('ingredient18_units'),
            'ingredient18_name': request.form.get('ingredient18_name'),
            'ingredient19_quantity': request.form.get('ingredient19_quantity'),
            'ingredient19_units': request.form.get('ingredient19_units'),
            'ingredient19_name': request.form.get('ingredient19_name'),
            'ingredient20_quantity': request.form.get('ingredient20_quantity'),
            'ingredient20_units': request.form.get('ingredient20_units'),
            'ingredient20_name': request.form.get('ingredient20_name')
        },
        'method': {
            'method_step1': request.form.get('method_step1'),
            'method_step2': request.form.get('method_step2'),
            'method_step3': request.form.get('method_step3'),
            'method_step4': request.form.get('method_step4'),
            'method_step5': request.form.get('method_step5'),
            'method_step6': request.form.get('method_step6'),
            'method_step7': request.form.get('method_step7'),
            'method_step8': request.form.get('method_step8'),
            'method_step9': request.form.get('method_step9'),
            'method_step10': request.form.get('method_step10')
        },
        'author': {
            'author_username': session['username'],
            'author_dob': session['user_dob'],
            'author_region': session['user_region']
        },
        'public_visibility': request.form.get('public_visibility')
    })
    return redirect(url_for('manage_creations'))
  
"""  
Checks if the cuisine contains recipes and if the new cuisine name already exists. 
If so prompts user to create a different cuisine type. Only unique cuisine types that have no recipes
added to them will be updated to MongoDB mLab Database.
"""  
@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])    
def update_cuisine(cuisine_id):
    page_title = 'Manage Your Creations | OneTwoCook'
    cuisines = mongo.db.cuisines.find({'_id': ObjectId(cuisine_id)})
    # recipes = mongo.db.recipes.find({"cuisine_type": cuisine_type})
    return render_template('manageyourcreations.html', cuisines = cuisines, page_title = page_title)
        
# Index of Recipes Page
@app.route('/index_of_recipes')
def index_of_recipes():
    page_title = 'Index of Recipes | OneTwoCook'
    caption = 'Below is a collection of all the recipes already available and visible to the public on this site.'
    all_public_recipes = mongo.db.recipes.find({'public_visibility' : 'on'}).sort('recipe_name', 1)
    return render_template('indexofrecipes.html', recipes = all_public_recipes, page_title = page_title, caption = caption)

# Index of Recipes Page - Filter for Gluten Free Recipes
@app.route('/index_of_recipes/gluten-free')
def gluten_free():
    page_title = 'Index of Recipes | OneTwoCook'
    caption = 'Below shows all gluten-free recipes that are already available and visible to the public on this site.'
    gluten_free = mongo.db.recipes.find({'gluten_free' : 'on'}).sort('recipe_name', 1)
    return render_template('indexofrecipes.html', recipes = gluten_free, page_title = page_title, caption = caption)
    
# Index of Recipes Page - Filter for Recipes suitable for Vegetarians
@app.route('/index_of_recipes/vegetarian')
def suitable_for_vegetarians_index():
    page_title = 'Index of Recipes | OneTwoCook'
    caption = 'Below shows all recipes suitable for vegetarians that are already available and visible to the public on this site.'
    vegetarians = mongo.db.recipes.find({'vegetarian' : 'on'}).sort('recipe_name', 1)
    return render_template('indexofrecipes.html', recipes = vegetarians, page_title = page_title, caption = caption)

# Viewing a Recipe from Index of Recipes Page
@app.route('/index_of_recipes/<recipe_id>/<recipe_name>')
def recipe_from_index(recipe_id, recipe_name):
    page_title = recipe_name + ' | OneTwoCook'
    view_recipe = mongo.db.recipes.find({'_id': ObjectId(recipe_id), 'recipe_name': recipe_name})
    previous_url = url_for('index_of_recipes')
    previous_page = 'Index of Recipes'
    return render_template('viewrecipe.html', recipes = view_recipe, previous_url = previous_url, previous_page = previous_page, page_title = page_title)
        
# Delete created Cuisine Type
@app.route('/delete_cuisine/<cuisine_id>/<cuisine_type>')
def delete_cuisine(cuisine_id, cuisine_type):
    cuisines = mongo.db.cuisines.find({'_id': ObjectId(cuisine_id)})
    recipes = mongo.db.recipes.find({"cuisine_type": cuisine_type})
    if len(recipes) > 0:
	    print("You can't delete this cuisine has it has multiple recipes associated with it")
	    return render_template('manageyourcreations.html', cuisines = cuisines, recipes = recipes)
    mongo.db.cuisines.remove({'_id': ObjectId(cuisine_id)})
    return redirect(url_for('manage_creations'))
    
# Delete a Recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('manage_creations'))

if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
        port = int(os.environ.get('PORT')),
        debug = True)