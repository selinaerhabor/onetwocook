# Data Centric Development Project: OneTwoCook – Online Cookbook
OneTwoCook is an interactive web application allowing users to enjoy access to a collection of cooking recipes. A user can choose to access the website as a guest or type in their name on the login page to get free and full access to create and edit their recipes online. This online cookbook aims to create a community to encourage the sharing of cooking recipes and explores the different cuisines people would like to share to others. The application is able to filter recipes into clear categories to make it easy to view. 

OneTwoCook can be accessed [here].

## List of Contents
1. [**User Experience Design (UX)**](https://github.com/selinaerhabor/onetwocook#1-user-experience-design-ux)
      
    1.1	[User Stories](https://github.com/selinaerhabor/onetwocook#11-user-stories)

    1.2	[Database Layout](https://github.com/selinaerhabor/onetwocook#12-database-layout)

    1.2.1 [Collections](https://github.com/selinaerhabor/onetwocook#121-collections)


2. [**Features**](https://github.com/selinaerhabor/onetwocook#2-features)
      
    2.1 [Existing Features](https://github.com/selinaerhabor/onetwocook#21-existing-features)

    2.1.1 [Create (**C**RUD) Features](https://github.com/selinaerhabor/onetwocook#211-create-crud-features)
    
    2.1.2 [Read (C**R**UD) Features](https://github.com/selinaerhabor/onetwocook#212-read-crud-features)
    
    2.1.3 [Update (CR**U**D) Features](https://github.com/selinaerhabor/onetwocook#213-update-crud-features)
    
    2.1.4 [Delete (CRU**D**) Features](https://github.com/selinaerhabor/onetwocook#214-delete-crud-features)
      
    2.2 [Layout and Overall Aesthetics](https://github.com/selinaerhabor/onetwocook#22-layout-and-overall-aesthetics)

    2.3 [Potential Features to Implement](https://github.com/selinaerhabor/onetwocook#23-potential-features-to-implement-in-the-future)

3. [**Technologies used**](https://github.com/selinaerhabor/onetwocook#3-technologies-used)

4. [**Testing**](https://github.com/selinaerhabor/onetwocook#4-testing)
      
      4.1 [Process of Testing Features](https://github.com/selinaerhabor/onetwocook#41-process-of-testing-key-features)

      4.2 [HTML and CSS Validation](https://github.com/selinaerhabor/onetwocook#42-html-and-css-validation-results)
      
      4.3 [Jasmine Test Results](https://github.com/selinaerhabor/onetwocook#43-jasmine-tests-results)
      
      4.4 [Device Screen Size and Browser Compatibility Test Results](https://github.com/selinaerhabor/onetwocook#44-device-screen-size-and-browser-compatibility-test-results)
      
      4.5 [Responses from users who tried out the OneTwoCook application](https://github.com/selinaerhabor/onetwocook#45-responses-from-users-who-tried-out-the-online-cookbook-application)
      
      4.6 [Interesting bugs or problems discovered during testing](https://github.com/selinaerhabor/onetwocook#46-interesting-bugs-or-problems-discovered-during-testing)

5. [**Deployment**](https://github.com/selinaerhabor/onetwocook/blob/master/README.md#5-deployment)
      
      5.1 [Deployment Process](https://github.com/selinaerhabor/onetwocook/blob/master/README.md#51-deployment-process)

      5.2 [Running the code locally](https://github.com/selinaerhabor/onetwocook/blob/master/README.md#52-running-the-code-locally)
      
      5.3 [Discussion on the differences between the development code and the deployed Code Version](https://github.com/selinaerhabor/onetwocook/blob/master/README.md#53-discussion-on-the-differences-between-the-development-code-and-the-deployed-code-version)

6. [**Credits**](https://github.com/selinaerhabor/onetwocook/blob/master/README.md#6-credits)
      
      6.1 [Content/Media](https://github.com/selinaerhabor/onetwocook/blob/master/README.md#61-contentmedia)

      6.2 [Acknowledgements](https://github.com/selinaerhabor/onetwocook/blob/master/README.md#62-acknowledgements)


## 1. User Experience Design (UX)

The aim of OneTwoCook is to provide users with an interactive cookbook application which has a creative flair and inspires users to create and share recipes on the application. The suggested age range for this application is 11 years and up. The brand name OneTwoCook is a play on the words ‘Want to Cook’, to provide users with a catchy and creative application brand. Some main highlights in the OneTwoCook application features include a personalised dashboard ‘Manage Your Creations’ where users can manage the recipes they’ve created, below this page users can also manage the cuisines they’ve created. Another interesting feature is the ability to cross out method steps after the user has completed the step, this makes it easier to keep track of cooking progress and avoid accidently repeating steps that will hinder recipe success.

Main Requirements for the Online Cookbook: 
* Should allow users to store and easily access recipes. 
* Application should logical database design.
* Allow users to add new recipes to the application.
* Should group and summarise the recipes on the site.
* Filter recipes based on various criteria.
* Create a detailed view for each recipe.
* Allow for editing and deleting of recipe records.

## 1.1 User Stories
I collected opinions from what users would like in an online cookbook. From gluten-free recipes to an interesting table of contents, I collected feedback from users who discussed potential features they wished to be taken into consideration prior to building the online cookbook application:

> "Contains vegan, gluten-free, and whole-foods plant-based recipe"

> "A cookbook with quality glossy photos beckons you to try something new"

> "Lots of great photos, easy-to-read large print"

> "Great illustrated step-by-step recipes on how to prepare all food from appetizers to dessert"

> "Should be engaging, with a unique reading style"

> "Creative, unique and open to your own additions"

> "Instructions must be clear enough to allow any cook to reproduce the results of the recipe author"

> "Comprehensive selection of recipes with an interesting table of contents"


The wireframes were based on meeting the project's requirements and the needs of users, covering each of the pages of the online cookbook from the home page to the logout page. Wireframes are available in this folder: [Initial Ideas - Wireframes].

## 1.2 Database Layout
For the OneTwoCook application, MongoDB mLab application was chosen as the platform to build a non-relational database structure.
The database currently has two collections - Recipes and Cuisines with a primary key of cuisine_type which appears in both collections.

### 1.2.1 Collections: 
* There are two collections in the database: **Recipes** and **Cuisines**.
* For the Recipes collection, embedded style structure has been used to ensure information collected from Add a Recipe 
form is neatly collated and easy to read when being displayed to users. One of the key requirements of users for the
cookbook is for a clear and easy to understand layout.

* Please see [Database Schema] Folder for details of collection database structure.

## 2. Features
OneTwoCook combines stylishness and user-friendliness in meeting the needs of users’ as an online cookbook. The overall aesthetics for the application are clean with white card panel backgrounds to avoid the overcrowding of style features so that every intended style feature can be appreciated. From the website navigation layout to the scoring out of recipe method steps when clicked on. The user stories were taken into account when building the features and components of the online cookbook. I have chosen a contrasting colour effect for this application to guide the users focus to the text and images displayed on the application. 

## 2.1 Existing Features 
### 2.1.1 Create (**C**RUD) Features
**Add a Recipe** 
* **Recipe Summary** - allows the recipe author to describe the recipe they have created, the recipe summary displays when user hovers over a recipe card. Recipe summary is limited to 180 characters, which allows the recipe summary to display on the recipe card (when hovered) without any text being cut off.
* **Required input fields** - adding the required attribute to input fields ensures that no users can submit an empty add a recipe form. For a user to submit a new recipe, they must ensure they complete all the required fields (cuisine type, recipe name, recipe summary, serves, allergens, at least 1 ingredient, at least 1 method step, author region). This ensures that the quality of recipes created by users are consistent in quality when viewing.
* **Scroll feature for Ingredients and Method sections** - Activated vertical scroll and restricted section to 150px for both sections. 
* **New Input field appears below last entry** - this feature is available for Ingredients and Method section to ensure the vertical overflow of information on the ‘Add A Recipe’ page is maintained in order to make it easier for the user to view through their entries on the different sections before submitting their recipe to the database.
* **Disabled username input field when creating recipe** - to ensure that the author username matches the username being used to create a new recipe.
* **’Gluten-free’ switch** - Can label a recipe gluten-free. Makes it easier for people with specific dietary requirements to find and create recipes that are suited to people who require gluten-free food.
* **’Suitable for Vegetarian’ switch** - Can label a recipe suitable for vegetarian. Makes it easier for people with specific dietary requirements to find and create recipes that are suited to vegetarians.
* **Public Visibility** - users can choose whether they want to make a recipe public or not for viewing. If public visibility is on (default), then recipe will appear on the site for everyone to see. If public visibility is off, then only the creator of the recipe will be able to view their recipe via ‘Manage Your Creations’.

**Add a Cuisine** 
* **Cuisine Type** - Adding a cuisine type will allow the user to select their newly created cuisine type from the dropdown list of cuisine type selections when adding a new recipe. This new cuisine will also display on the home page which lists all cuisines created. A cuisine created by OneTwoCook uses a selected image, but a cuisine created by a user is distinguished by being displayed with coverphoto_other (wooden cutlery image). This allows the application to control the cover photo selected for new cuisine types creations and ensures that a cuisine cover photo does not fail. This also makes it a creative way to notice how the online community on the application is growing and encourage other OneTwoCook users to create new cuisines and recipes on the site. 
* **Cuisine Summary** - allows the cuisine author to describe the cuisine they have created, the cuisine summary displays when user hovers over a cuisine card.
* **Login Page** - When a user visits the OneTwoCook website, they are prompted on whether they would like to create a username to get full access to create and edit recipes or whether they would like to continue as a guest. I believe giving the user room for choice makes it effective to deliver features they want to see. For example, a user who wants to simply ‘continue as a guest’ is likely to be solely interested on the cuisines and recipes available to the public on the website. The OneTwoCook login page requires users to fill in their name (also display name), birth date (for user identification purposes) and region (display region). Including entry for birth date ensures users are uniquely identified. For this project, the authentication process is not secure. 


### 2.1.2 Read (C**R**UD) Features
* **Back to previous page link** - For every page on the online cookbook there is a ‘back to previous page’ link underneath the page’s title which will take the user back to the previous page. This will remind the user of how they have navigated through the online cookbook and eases navigation across the site.

**Cuisine Selection - Viewing recipes for cuisine** 
* **Home Page** - On this page, the various cuisine types available on the site are displayed in alphabetical order (descending). The home page has been built with 12 cuisines with specific cover photos and 1 cuisine (Greek) with a default cover photo. The reason behind this, is to ensure all cuisines listed on the home page have images displayed. The Greek cuisine was created as an example to show how cuisines created by user will appear on the home page. When a user hovers over a cuisine type, the cuisine card glows and the cuisine summary appears. When they click on the cuisine type, they will be redirected to ‘recipes for cuisine’ page.
* **Recipes for Cuisine Page** - displays the list of recipes visible to the public for the selected cuisine, when the user hovers over the recipes, the recipe card glows and the selected recipe’s summary displays. When the user clicks on a recipe, this will display the details of the selected recipe. In the event of no recipes present for your selected cuisine, there is an Add a Recipe button on the page which will redirect users to the Add a Recipe form (also accessed via navigation bar at top of page). If there are recipes present for the selected cuisine, ‘+’ button is available next to the page title to allow users to create recipes via link. During testing the application with users, some users who created recipes via Add a recipe button on recipes_for_cuisine page pointed out that there needs to be direction on where to create a recipe when the Add Recipe button disappears after a recipe has been added to the recipes_for_cuisine page.

**Recipe Selection - Viewing individual recipe** 
* **Click on a completed method step to strikethrough** - Toggle feature which allows users to cross out method steps they have completed. This makes it easier to remember where you are in the cooking process and not to repeat any steps by mistake. If a user mistakenly crossed out a step, if they click on it again the strikethrough will be removed hence why I have chosen to use it as a toggle feature. 
* **Thumb Up** - When a user clicks on the thumb up symbol for a recipe, that will increase the recipe thumb up count by 1 and the recipe card will be copied to the user’s ‘Saved Recipes’ dashboard on ‘Manage Your Creations’ page.
* **Logout Page** - The logout button closes the session for the current username and redirects users to the login page via ‘Return to Homepage’ button.
* **Print Icon** - clicking on the print icon (from material icon) is situated underneath a recipe page. The print icon will activate the print preview and settings page to allow the user to print out the recipe. This feature is available for both guest viewers and users who created a username.
* **Twitter Icon** - Allows users to tweet about their experiences using the OneTwoCook application by using #OneTwoCook. This will help raise awareness of the brand and encourage more people to join the site to help build up the online community. This icon is situated just above the footer on the viewrecipe.html page.

**Manage Your Creations Page**
* **Recipe Count** - counts the number of recipes created by user
* **Manage Your Recipes** - lists recipes created by user in card format, with options to view, edit or delete the recipe.
* **Cuisine Count** - counts the number of cuisines created by user
* **Manage Your Cuisines** - lists cuisines created by user in card format, with options to view, edit or delete the cuisine.
* **Saved Recipes** - this section currently displays default no recipes saved message. As a feature to implement in the future (see 2.3 Features Left to implement), this section will list recipes saved by the user in card format.





### 2.1.3 Update (CR**U**D) Features
Access to editing recipes and cuisines made by a user is restricted to only users who have created a username and have created a recipe/cuisine. These features can be found under the Manage Your Creations page. (Please note this feature is not available for guest users).

**Manage Your Creations Page** 

**Manage Your Recipes Section** 
This page displays the list of recipe types (in a card form) created by the username.
* **More symbol** - reveals Edit and Delete buttons for each recipe/cuisine created by the user
* **Edit created recipe** - allows user to make changes to the recipe they created. They can edit their cuisine type, recipe name, recipe summary, serves, allergens, ingredients, method and public visibility. After changes have been made and user clicks submit, the recipe will be updated in the database.

**Manage Your Cuisines Section** 
This section is found under the Manage Your Creations section and displays the list of cuisine types (in a card form) created by the username.
* **Edit created cuisine** - allows user to make changes to the cuisine they created. They can edit their cuisine type and cuisine summary. After changes have been made and user clicks submit, the cuisine will be updated in the database. All cuisine types created are made public.


* **Saved Recipes Section** 
This section allows user to save recipes from selection of recipes available for public viewing by clicking on the thumb up icon.


### 2.1.4 Delete (CRU**D**) Features
Access to deleting recipes and cuisines made by a user is restricted to only users who have created a username and have created a recipe/cuisine. These features are not available for guest users.

* **Delete recipe** - initiates modal to confirm whether the user is sure they would like to delete the selected recipe. If the user clicks ‘YES’ the selected recipe will be deleted, but if the user clicks ‘NO’ the selected recipe will not be deleted and the user will be returned to the ‘Manage Your Creations’ page.
* **Delete cuisine** - initiates modal to confirm whether the user is sure they would like to delete the selected cuisine. If the user clicks ‘YES’ the selected cuisine type will be deleted, but if the user clicks ‘NO’ the selected cuisine will not be deleted and the user will be returned to the ‘Manage Your Creations’ page.



### 2.2 Layout and Overall Aesthetics
* **Brand Logo** - the brand logo is intended to create an attitude to get ready to cook, with the numbers 1 and 2 symbolising the two selections that have to be made to view a recipe. Two selections – Select a Cuisine Type > Select a Recipe.
* **Website Icon** - used the ‘1’ from the OneTwoCook logo as the website icon. With the number one referring to the first step in finding a recipe in the cookbook (home page contains a list of all the cuisines available on the site).
* **Personalised Welcome message on home page** - welcomes guest/full access user. If guest view only ‘Welcome’ will be displayed, if username is created ‘Welcome <username appears here>!’ will be displayed.
* **Side Navigation Bar (Mobile view)** - available on mobile view, displays username and the different pages on the website to make it easy to navigate through the site.

## 2.3 Potential Features to implement in the future:
Currently, the Twitter button available at the bottom of recipe pages, allows users to tweet using #OneTwoCook to post their cooking outcomes on social media. The addition of a section to feed in the social media posts from twitter from users using #OneTwoCook, will be useful in connecting pictures of the dish outcomes from following the recipes on the website. This feature may be useful as I believe it will make the website more engaging to users therefore enhancing user experience.  

The Thumb Up button on the top of recipe pages and the Saved Recipes Section are mock features which will be implemented in the future to allow users to list a recipe card they have clicked thumb up button in their Saved Recipes section (Manage Your Creations page). Feature will also allow them to remove recipes off from their Saved Recipes list.


## 3. Technologies Used
*  	[AWS Cloud9] - The Integrated Development Environment (IDE) used for building the website.
*	[HTML] - Used for the structure and format of the entire website.
*	[CSS] - For styling the website and maintaining its responsiveness across various screen sizes.
*	[Materialize] - Used for grid form and assistance in styling.
*	[JQuery] - Used for the interactive features of the online cookbook to enhance user experience.
*	[Material Icon] - Used for displaying the social logos and vector icons present on the website.
*	[Browsershots.org] - For checking browser compatibility and cross platform browser testing.
* 	[Jasmine CDNJS] – For testing key sections of jQuery code for the online cookbook.
*	[W3C HTML Validator] - Used to check that no errors were present in the HTML code before final deployment.
*	[W3C CSS Validator] - Used to check that no errors were present in the CSS code before final deployment.
*	[JSHint] - Used to check code quality of JavaScript code.

## 4. Testing
This section discusses the testing process of key features of the OneTwoCook online cookbook and documents test results on various device screen sizes and browsers to ensure the application is responsive.

## 4.1 Process of Testing Key Features:

**Login – Create Username**

* Opened OneTwoCook application and was directed to the login page [login.html]
* Typed in name (max. 15 characters)
* Typed in date of birth
* Selected Region from dropdown list
* Submitted name, date of birth and region and was then redirected to welcome home page.
*Tried clicking submit button with only one of the three fields completed and was prompted to complete the remaining input fields in order to submit. 


**Home – Cuisine selected**

* After a successful login, a list of all cuisine cards will be displayed on the home page below the welcome greeting.
* Hovered over each cuisine and their respective cuisine summary appeared over the image of the cuisine card and the cuisine card glows.
* When the cuisine card is selected, a list of all recipes that have been set to public are displayed on a new web page.


**Recipe Selection **

* Hovered over each recipe available for the cuisine and their respective recipe summary appeared over the recipe image and the recipe card glows.
* Selected a recipe and redirected to a new web page showing all details of the recipe. 
* Crossed out completed method steps by clicking on them.

**Creating a Recipe for public viewing (Username only)**

* Clicked the ‘Add a Recipe’ tab
* Filled in all recipe details
* Left the ‘Make recipe public’ switch checked (YES) 
* Returned to home page [index.html]
* Clicked on the cuisine type, I created my recipe for
* Newly created recipe appearing on results


**Creating a Recipe for private viewing (Username only)**

* Clicked the ‘Add a Recipe’ tab
* Filled in all recipe details
* Changed the ‘Make recipe public’ switch to NO (public_visibility = null) 
* Returned to home page [index.html]
* Clicked on the cuisine type, I created my recipe for
* Newly created recipe not appearing on results

**Editing a Recipe (Username only)**

* Clicked the ‘Manage Your Creations’ tab
* Clicked the more symbol (three dots) on the recipe card and revealed the View, Edit and Delete buttons
* Clicked the Edit button and edit page for the recipe loaded up
* Changed the recipe summary and changed ‘Make recipe public’ switch from YES to NO
* Clicked on the cuisine type I created my recipe for, using Home page tab
* Edited recipe no longer appearing on public results (public visibility = null), 


**Add a Cuisine (Username only)**

* Clicked the ‘Add a Recipe’ tab
* Clicked the ‘Add cuisine’ button
* Typed in Cuisine type in input field
* Typed in Cuisine summary in input field
* Clicked Submit and redirected back to ‘Add a Recipe’ page
* Newly created cuisine now appearing in dropdown field for cuisine type and appearing on home page.


**Manage Your Creations (Username only)**

* Selected ‘Manage Your Creations’ tab on the navigation bar
* Clicked the ‘Manage Your Recipes’ and redirected to Manage Your Recipes section listing all recipes I have created. 
* Clicked the ‘Manage Your Cuisines’ and redirected to Manage Your Cuisines section listing all cuisines I have created. 
* Clicked the ‘Saved Recipes’ and redirected to Saved recipes section listing all recipes I have saved. 


**Manage Your Recipes (Username only)**

* Selected ‘Manage Your Recipes’ from box option on the Manage Your Creations page
* Scrolled down to a recipe I created
* Clicked the more symbol (three dots) and for recipes set to private viewing the options are the ‘View’, ‘Edit’ and ‘Delete’ buttons. For recipes set to public viewing the options are ‘Edit’ and ‘Delete’ buttons. 
* Clicked ‘Delete’ button and delete modal prompt appears
* Clicked YES and recipe is deleted



**Manage Your Cuisines (Username only)**

* Selected ‘Manage Your Cuisines’ from box option on the Manage Your Creations page
* Scrolled down to ‘Manage Your Cuisines’ section and selected a cuisine I created
* Clicked the more symbol (three dots) and for cuisines the options are ‘Edit’ and ‘Delete’ buttons. 
* Clicked ‘Delete’ button and the delete modal prompt appears
* Clicked YES and cuisine is deleted



## 4.2 HTML and CSS Validation Results:
The HTML and CSS code for the OneTwoCook application has been tested using official validators, screenshots of the Browser Test results are available via the links below and can also be found in a folder called `browser-tests` under the `tests` folder.

**HTML code**
* No major application errors returned for HTML code for OneTwoCook Online Cookbook.

**CSS Code**
* No major application errors returned for the CSS code for OneTwoCook Online Cookbook. 


## 4.3 Jasmine Tests Results: 
The Jasmine tests that were carried out for the application include, how OneTwoCook produces new input fields below when a user has made an entry in the field above, testing toggle feature of scoring out method steps and a test for inputting recipe image URLs. 

**New input field appearing below:** 
* This test demonstrated whether the application was correctly calling the next input field whenever the user made an entry in an input field above. 

* This test demonstrated whether the hint function correctly recalls the last selected buzzer ID. For this test, I declared 
an example selection of buzzers up to level 6. The buzzers are symbolised by ID numbers (0, 1, 2 and 3).

**Method step strikethrough toggle:**
* This test demonstrated whether the application was correctly calling the score feature whenever the user clicked a method step listed on the recipe page. 
* For the first test, I declared the variable for the game's moves and another variable to select a buzzer ID at random. The test 
checked that the buzzer ID selected at random by the game is between 0 and 3.
* For the second test, I declared a variable which is a representation of having multiple classes in a `<div>`. This test checked that the 
game correctly reads the squareColor class using the `.split()` method and therefore assign the right style properties to the buzzer.

**Recipe Image URL:**
* This test demonstrated whether the application was correctly reading the URL submitted by the user via the Add a Recipe form. 
* This test demonstrated whether the game can correctly select the corresponding audio file from a buzzer ID. For this test, I declared 
the buzzer IDs, four example audio files in an array and a sound player variable which uses the index of an array to map it to each buzzer. 
This test checked that the game correctly selects a buzzer's matching audio file so the right buzzer sound plays upon selection.

Overall, the results from testing the application shows that the correct variables are being selected. 
Screenshot of the [Jasmine Test Results Page] and the script for the main JavaScript code (onetwocook.js) had no major issues appear in JSHint Quality tool.


## 4.4 Device Screen Size and Browser Compatibility Test Results:
* The below screen size tests were carried out assessing performance of all pages of the website using Google Chrome 74.0 (Windows):

Device | Screen Size (Width x Height) | OneTwoCook
---- | ---- | ---- | 
Galaxy S5 | 360 x 640 | ✓ | 
Pixel 2 | 411 x 731 | ✓ |
Pixel 2 XL | 411 x 823 | ✓ |  
iPhone 5 SE | 320 x 568 | ✓ | 
iPhone 6/7/8 | 375 x 667 | ✓ | 
iPhone 6/7/8 Plus | 414 x 736 | ✓ | 
iPhone X | 375 x 812 | ✓ | 
iPad | 768 x 1024 | ✓ | 
iPad Pro | 1024 x 1366 | ✓ | 
Sony Bravia Television 4K |5280 width (55")|✓ | 

In addition, the website has also been tested on other browsers including Firefox and Google Chrome at the various screen sizes using [Browsershots.org]. This allowed me to test the online cookbook application on Linux and Windows operating systems. Below are the test results of the website deployed on Heroku when tested on Browsershots.org on various browsers. 

Key screenshots of the Browser Test results can be found in the `tests` folder.
* Key: ✓ - Application loads successfully

Operating System | Browser | OneTwoCook 
---- | ---- | ---- | 
Linux | Firefox 61.0 | ✓ | 
Windows | Firefox 66.0 | ✓  | 
Windows | Chrome 71.0 | ✓  |

Overall, the results of the tests documented in this chapter and feedback from users testing the application suggests that OneTwoCook works very well across key operating system browsers and various screen sizes with the application layout and structure adjusting responsively. The online cookbook application should therefore be reliable and easy to use on various devices. 


## 4.5 Responses from users who tried out the online cookbook application:
I asked a group of people to try out the OneTwoCook Application. They were given the opportunity to try using the application in both guest mode and full access user mode. This allowed the users to experience the application from two different viewpoints, get a better understanding of the application and its features and possibly come to a conclusion on which mode they preferred. 

The responses demonstrated success in meeting the user requirements initially set out in the design brief and discussed in the user stories (see 1.1 User Stories). Below are some of the feedback received from the users:

> "Very engaging, will definitely be visiting again"

> "This really suits my style"

> "Very nicely designed"

> "Looks stylish and a clever concept"
 
> "Great quality application with great features"


## 4.6 Interesting bugs or problems discovered during testing:
1. Previously, if a user wanted to view a recipe they created via Manage Your Creations page they would be redirected to the view recipe page, but with a back to previous page link of Recipes for Cuisine which was not correct. I decided to create a new app route using the viewrecipe.html template and making the back to previous page link a variable. I then used jinja syntax in if statements to call the variable in the templates accordingly as shown below.


```sh
{% if previous_url == 'recipes_for_cuisine' %}
<a class="left" href="{{url_for('recipes_for_cuisine', cuisine_type = recipe.cuisine_type)}}"><i class="material-icons left">arrow_back</i>Back to {{recipe.cuisine_type}} Recipes</a>
{% else %}
<a class="left" href="{{previous_url}}"><i class="material-icons left">arrow_back</i>Back to {{previous_page}}</a>
{% endif %}
```
The above code ensures that if a user views a recipe via the Recipes for Cuisine page then the back to previous page url will redirect users to the list of recipes for the cuisine they chose at the home page. If the user is viewing via Manage Your Creations the url and page link name will also change accordingly. This allows the user to keep track of their path through the website and redirect them to where they wish to navigate to next.

2. When a user clicked on ‘Edit Recipe’ button via Manage Your Recipes, the public visibility switch returns to default “on”. This means when editing a recipe, the recipe will become public unexpectedly when changes are saved. In order to fix this, I added the below for the switch to be adjusted to last saved update of switch.

```sh
{% if public_visibility == “on” %}
  
{% else %}

{% endif %}
```
3. Two recipes with the same name were being loaded together on one page. To prevent this, the addition of the recipe_id variable being called alongside the recipe_name made the query call the specific recipe despite similarities with others. The code is displayed below:

```sh
view_recipe = mongo.db.recipes.find({'_id': ObjectId(recipe_id), 'recipe_name': recipe_name})
```

4. When a cuisine with the same name as an existing cuisine has been created, this will duplicate all recipes in the existing cuisine to also appear in the created cuisine. In order to prevent this, I have amended the add_cuisine definition to create a block when a user tries to create a cuisine with the same name as an existing cuisine type. 

```sh
cuisines = mongo.db.cuisines.find_one({ 
        "cuisine_type": 
            {"$regex": request.form.get('cuisine_type'),
            "$options":"i"}
        })
    if cuisines:
        alert = "*The cuisine type you entered already exists. Please choose another cuisine.*"
        return render_template('addcuisine.html', alert = alert, cuisines = cuisines)
```

5. When a user presses the delete button on a recipe/cuisine, they are prompted with a delete confirmation modal on whether they are sure they wish to delete the selected recipe/cuisine. The delete confirmation modal was created for as many times as there were recipes, but as the modal id was set to `deleteModal`, whenever the delete button was pressed it would call the modal for the first recipe/cuisine created by the specific user instead of calling the modal for the selected recipe/cuisine. In order to fix this, the modal id was changed to call the selected recipe name using jinja syntax as seen below.

```sh

<!--Code snippet from Delete Confirmation Modal-->
<div id="delete{{recipe.recipe_name}}" class="modal">...</div>

<!--Code snippet from Delete Button -->	
<a class="waves-effect waves-light red btn modal-trigger manager" href="#delete{{recipe.recipe_name}}">Delete<i class="material-icons right">delete</i></a>

```


6. When a user deletes/edits a cuisine it is removed completely from the database. Recipes which were attached to the deleted/edited cuisine get lost in the database and can no longer be viewed on the website until the cuisine type is recreated. In order to prevent this, I have added two new functions check_before_delete and check_before_edit to create a block when a user tries to edit/delete a cuisine which has recipes attached to it. Users can now only delete/edit cuisines they have created which do not have any recipes attached to it. 

```sh
cuisine_has_recipes = mongo.db.recipes.find({"cuisine_type": cuisine_type}).count()
    if cuisine_has_recipes:
        messages = 'Recipes have been found. This cuisine cannot be edited/deleted.'

``` 


## 5. Deployment
## 5.1 Deployment Process:
For deploying OneTwoCook to Heroku:
*Firstly, type into AWS Cloud9 terminal the command `pip freeze > requirements.txt` to create a requirements.txt file. 
*Then, type into AWS Cloud9 terminal the command `echo web: python app.py > Procfile` to create a Procfile. 
*Use commands - `git add` and then `git commit` to apply the changes to the application, then use `git push` to push the project to GitHub.
*Create a new app where the OneTwoCook Application will be deployed on the Heroku website by clicking on the button called "New" in your Heroku dashboard. 
*Set the app-name and the region to your respective region. 
*Next, click on Settings > Reveal Config Vars. Set the IP, PORT, MONGO_URI and Secret_Key config vars in Heroku:

```sh
**Key**  Value
**IP**    - 0.0.0.0
**PORT**  - 5000
**MONGO_URI** - mongodb://<dbuser>:<dbpassword>@ds213665.mlab.com:13665/[mLab database-name]
**SECRET_KEY** - <secret key goes here>
```
Type in the command below to log into your Heroku account via AWS Cloud9 terminal
```sh
$ heroku login
```
*Type in your Heroku credentials
*If changes are made to the cloned version of code, make a git commit and push changes to GitHub using the by typing the below commands in your AWS Cloud9 terminal:
```sh
$ git add .
$ git commit -am "type reason for changes to your code here"
$ git push
```
*After changes have been pushed to GitHub, type in command ` git push heroku master` to push the updated code to Heroku.
*Verify whether application has been correctly built by clicking on More > View Logs. 
*Application should now be up and running at https://app-name.herokuapp.com/
## 5.2 Running the code locally:
The repository for this website can be cloned using the command below in AWS Cloud 9 workspace terminal:

```sh
$ git clone https://selinaerhabor.github.io/onetwocook.git
```
*Type in the command `python3 app.py` in AWS Cloud9 terminal and open the app.py file to run the OneTwoCook application.

## 5.3 Discussion on the differences between the development code and the deployed Code Version:
* The home page was previously one cuisine card per row, but this longer form of the cuisine card left excess space around content and did not seem to use space efficiently. The home page now allows up to three cuisine/recipe cards per row, making it easier for users to browse through all the cuisine types/recipes available to the public and make a more informed decision.                                                                          

* Originally, all recipe cards on the website were to have the more symbol (three dots) along the edge of the cuisine/recipe card, when clicked the recipe summary will be revealed in a slide up effect. However, when the application was tested by users, they expected the more symbol to reveal settings features for edit options. After receiving the feedback, I decided to remove the card reveal feature from the home page and recipes for cuisine pages, but kept the more symbol feature for the Manage Your Creations page where the cards reveal View, Edit and Delete options. The cuisine and recipe cards displayed on the home page and Recipes for Cuisine pages when hovered now reveal an overlay with recipe summary appearing.

* Cuisine types created by users, have a default picture of wooden cutlery. Due to the list of cuisines available on the site being the home page of OneTwoCook it is important that all cuisines have great quality images present. In the case of a Cuisine Image URL failing, there would be a cuisine card with no image available, which will deter the aesthetics of the homepage. This is the reason why cuisine cover photos have been directly uploaded to the application. With this fix in place, no cuisine card should be created without a displayed cover photo.

* Removed the Add input field button from the website and used a more creative approach which adds new ingredient fields and method steps fields using JQuery. When the Add a Recipe page is loaded, all fields except the first rows for Ingredients and Method steps are hidden. Once the user begins to type in the first ingredient name/method step field, another field will become visible below it. So the user does not have to worry about adding a new field.

* The number of Ingredient input fields have been limited to 20, whilst the number of Method step fields have been limited to 10. The reason for these limits in user input is to ensure recipes are kept engaging and clear enough for users to follow. A recipe with structured in this way will encourage users who create recipes to phrase instructions in the best way therefore making the recipes produced clear and easy to follow for others.

* Users can view their recipes that are only visible to them (due to setting public_visibility to null) via the Manage Your Creations page. Viewing recipes on this page also makes it easier to check recipe again before editing and making amendments.

## 6. Credits
## 6.1 Content/Media:
**Sources**:
* Materialize Documentation - https://materializecss.com/getting-started.html
* Majority of recipes inspired from Olive Magazine, Naija Chef and BBC Good Food. 
* Allergens list (also accessible on application via Need Help button on Add a Recipe page) – https://www.food.gov.uk/business-guidance/allergen-guidance-for-food-businesses
* Ingredient Units - https://www.dummies.com/food-drink/recipes/measurement-abbreviations-and-conversions/
* Recipe Image URLs and Cuisine cover-photos were taken from Google Images.

## 6.2 Acknowledgements:

I would like to thank my mentor Aaron and all the tutors at Code Institute for taking time to explain good coding practices in tackling bugs within my application. 

[Return to top](https://github.com/selinaerhabor/onetwocook/blob/master/README.md#data-centric-development-project-OneTwoCook--online-cookbook)

[//]: # (Below are the reference links used in the body of the README file)
[here]: <https://onetwocook.herokuapp.com/>
[HTML]: <https://html.com/> 
[CSS]: <https://https://en.wikipedia.org/wiki/Cascading_Style_Sheets> 
[AWS Cloud9]: <https://aws.amazon.com/cloud9/>
[Browsershots.org]: <http://browsershots.org/>
[Material Icon]: <https://material.io/resources/icons/?style=baseline/>
[Materialize]: <https://materializecss.com/>
[Jasmine CDNJS]: <https://cdnjs.com/libraries/jasmine>
[Cookie]: <https://fonts.google.com/specimen/Cookie?selection.family=Cookie>
[Courgette]: <https://fonts.google.com/specimen/Courgette?selection.family=Courgette>
[JQuery]: <https://jquery.com/download/>
[W3C HTML Validator]: <https://validator.w3.org/>
[W3C CSS Validator]: <http://jigsaw.w3.org/css-validator/>
[Initial Ideas - Wireframes]: <https://github.com/selinaerhabor/onetwocook/tree/master/static/wireframes>
[JSHint]: <https://jshint.com/>
[Database Schema]: <https://github.com/selinaerhabor/onetwocook/tree/master/database_schema>
