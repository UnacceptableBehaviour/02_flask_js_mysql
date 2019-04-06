from flask import Flask, render_template, request
app = Flask(__name__)

from helpers import get_csv_from_server_as_disctionary, get_recipe_ingredients_and_yield, create_recipe_info_dictionary, inc_recipe_counter, log_exception
import pprint
import random

@app.route('/')
def hello_world():
    headline_py = "Biting the Toad"
    return render_template("nav_buttons.html", headline=headline_py, sub_headline='TeMpLaTe ChEcK . . ') #, info=info)

@app.route('/nutrient_table')
def nutrient_table():
    headline_py = 'Nutrients Table Solo'
    info = {}   # test undefined
    #info = get_nutrients_per_serving()
    
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
    
    #return render_template("nutrient_traffic_lights_page.html", headline=headline_py, info=info)
    return render_template("nutrient_traffic_lights_page.html", headline=headline_py, info=nutrients)

@app.route('/recipe_page')
def recipe_page():

    sql_dict = get_csv_from_server_as_disctionary()    
    
    for k, v in sql_dict.items():
        print(f"> > > K:{k} - V:{v['recipe_title']} {k.__class__.__name__}")
    
    rcp_id = 23
    
    updated_info = create_recipe_info_dictionary(sql_dict, rcp_id)
    
    headline_py = f"Recipe Page"
        
    return render_template("recipe_page.html", headline=headline_py, info=updated_info, image_dict=sql_dict)



@app.route('/picker')
def picker_page():
    print("PICKER PAGE ENTRY POINT")
    sql_dict = get_csv_from_server_as_disctionary()    
    
    entries = len(sql_dict)
    print(f"sql_dict.size: {len(sql_dict)}")
        
    
    #rcp_id = random.randint(0,entries-1)    
    rcp_id = inc_recipe_counter(entries)
    
    updated_info = create_recipe_info_dictionary(sql_dict, rcp_id)

    print(f"RECIPE id:{rcp_id}")
    
    return render_template("picker_page.html", headline='Toad head: Kaplooey. thud . . squirg', info=updated_info, rcp_id=rcp_id)