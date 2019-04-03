from flask import Flask, render_template, request
app = Flask(__name__)

# importing files
# https://realpython.com/absolute-vs-relative-python-imports/
# https://stackoverflow.com/questions/4142151/how-to-import-the-class-within-the-same-directory-or-sub-directory
# https://pep8.org/#imports
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3

#from .helpers import  load_csv_data, get_nutridata, get_nutrients_per_serving, get_ingredients_from_recipe
#ingredient_text_list = get_ingredients_from_recipe('mushroom rissotto')


from flask import Flask, render_template
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# giza a look
from pprint import pprint

import urllib.parse
#url_encoded_pwd = urllib.parse.quote_plus("kx%jj5/g")


# default
#engine = db.create_engine('dialect+driver://user:pass@host:port/db')
#engine = create_engine('mysql://root:meepmeep@localhost:3306/nutridb_sr25_sanitized')
#db = scoped_session(sessionmaker(bind=engine))

# 
# # each app.route is an endpoint
# @app.route('/db_test')
# def data_base_test():
#     # execute this query
#     # SELECT ndb_no, nutr_no, nutr_val, deriv_cd FROM nutrientdata ORDER BY nutr_val LIMIT 10;
#     #db_lines = db.execute("SELECT ndb_no, nutr_no, nutr_val, deriv_cd FROM nutrientdata ORDER BY nutr_val LIMIT 10;").fetchall()
#  
#     formatted_text = "<br>"
#     
#     #for line in db_lines:
#         #print(f" | {line.ndb_no} | {line.nutr_no} | {line.nutr_val} | {line.deriv_cd} | ")
#         #formatted_text = formatted_text + f" | {line.ndb_no} | {line.nutr_no} | {line.nutr_val} | {line.deriv_cd} | <br>"
#     
#     print(f"\n\nProcess Query {formatted_text}")
#     
#     return f"Processed Query:<br>{formatted_text} <br>END"
#     


@app.route('/')
def hello_world():
    headline_py = "Lick the Toad"
    #info = get_nutrients_per_serving() 
    #return render_template("picker_t.html", headline=headline_py) #, info=info)
    return render_template("nav_buttons.html", headline=headline_py, sub_headline='TeMpLaTe ChEcK . . ') #, info=info)
    #return "<h1>HELLO WORLD!</h1>"

@app.route('/nutrient_table')
def nutrient_table():
    headline_py = 'Nutrients Table Solo'
    info = {}
    #  // struct / JSON
    nutrients = {
      'rcp_id': 6,
      'recipe_title': 'Light Apricot Cous Cous',
      'n_En': 154.0,
      'n_Fa': 3.12,
      'n_Fs': 1.33,
      'n_Su': 2.93,
      'n_Sa': 0.58,
      'serving_size': 190.0
    };
    #info = get_nutrients_per_serving()    
    return render_template("nutrient_traffic_lights_page.html", headline=headline_py, info=nutrients)



# @app.route('/recipe_drop_down', methods=["GET", "POST"])
# def recipe_drop_down():
#     if request.method =='GET':
#         info = load_csv_data()
#         image_file = ''
#         headline_py = "Pick a Recipe"
#         return render_template("recipe_dropdown.html", headline=headline_py, recipe_image=image_file, image_dict=info)
#     else:           # POST
#         info = load_csv_data()
#         headline_py = "Pick a Recipe"        
#         image_file = request.form.get("recipe_image_list_drop_down")
#         return render_template("recipe_dropdown.html", headline=headline_py, recipe_image=image_file, image_dict=info)
#         

# @app.route('/drop_down_action', methods=["GET", "POST"])
# def drop_down_action():
#     if request.method =='GET':
#         return "THIS IS A GET REQUEST"
#     else:            
#         image_file = request.form.get("recipe_image_list_drop_down")
#         return render_template("show_image.html", recipe_image=image_file)
# 
# @app.route('/ingredients', methods=['GET','POST'])
# def ingredient_list():
#     header = 'rcp_id,image_filename,recipe_title,txt_ingredient_file,n_En,n_Fa,n_Fs,n_Fm,n_Fp,n_Fo3,n_Ca,n_Su,n_Fb,n_St,n_Pr,n_Sa,n_Al,serving_size'
#     info = {}
#     recipe_name = 'mushroom rissotto'
#     info['recipe_title'] = recipe_name
#     info['ingredient_list'] = get_ingredients_from_recipe(recipe_name)
#     #info['image_filename'] = get_image_for_recipe(recipe_name)
#     info['image_filename'] = './static/recipe/20190301_145910_mushroom rissotto.jpg'
#     
#     if request.method =='GET':      # arrive at page
#         return render_template("ingredients_list.html", info=info, ingredient_list=ingredient_text_list)
#     else:                           # page updating with user input request.method = 'POST' 
#         new_ingredient = request.form.get("form_ingredients_list")
#         ingredient_text_list.append(new_ingredient)
#         return render_template("ingredients_list.html", info=info, ingredient_list=ingredient_text_list)


#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port= 8090)
