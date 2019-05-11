#! /usr/bin/env python

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
      'ri_id': 6,
      'ri_name': 'Light Apricot Cous Cous',
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
        print(f"> > > K:{k} - V:{v['ri_name']} {k.__class__.__name__}")
    
    ri_id = 23
    
    updated_info = create_recipe_info_dictionary(sql_dict, ri_id)
    
    headline_py = f"Recipe Page"
        
    return render_template("recipe_page.html", headline=headline_py, info=updated_info, image_dict=sql_dict)



@app.route('/cycle')
def cycle_recipes():
    print("CYCLE THROUGH RECIPES")
    sql_dict = get_csv_from_server_as_disctionary()
    
    entries = len(sql_dict)
    print(f"sql_dict.size: {len(sql_dict)}")        
    
    #ri_id = random.randint(0,entries-1)    
    ri_id = inc_recipe_counter(entries)
    
    updated_info = create_recipe_info_dictionary(sql_dict, ri_id)

    print(f"RECIPE id:{ri_id}")
    
    return render_template("picker_page.html", headline='Toad head: Kaplooey. thud . . squirg', info=updated_info, ri_id=ri_id)


@app.route('/picker')
def picker_page():
    print("PICKER PAGE ENTRY POINT")
    sql_dict = get_csv_from_server_as_disctionary()
    
    entries = len(sql_dict)
    print(f"sql_dict.size: {len(sql_dict)}")        
    
    #ri_id = random.randint(0,entries-1)    
    ri_id = inc_recipe_counter(entries)
    
    updated_info = create_recipe_info_dictionary(sql_dict, ri_id)

    print(f"RECIPE id:{ri_id}")
    
    return render_template("picker_page.html", headline='Toad head: Kaplooey. thud . . squirg', info=updated_info, ri_id=ri_id)


@app.route('/picker_flask', methods=["GET", "POST"])
def picker_flask():
    sql_dict = get_csv_from_server_as_disctionary()
    
    if request.method =='GET':
        ri_id = 2
        
        headline_py = "Pick a Recipe (Flask) Opening"
        
        updated_info = create_recipe_info_dictionary(sql_dict, ri_id)
        
        return render_template("picker_flask.html", headline=headline_py, info=updated_info, sql_dict=sql_dict, ri_id=ri_id)

    else:           # POST
        headline_py = "Pick a Recipe (Flask)"
        ri_id = 2
        
        you_picked = request.form.get("recipe_list_drop_down")
        
        # brute force for expedience POC
        for recipe_no, recipe_info in sql_dict.items():
            if recipe_info['ri_name'] == you_picked:
                ri_id = recipe_no
        
        updated_info = create_recipe_info_dictionary(sql_dict, ri_id)

        return render_template("picker_flask.html", headline=headline_py, picked=you_picked, info=updated_info, sql_dict=sql_dict, ri_id=ri_id)



if __name__ == '__main__':
    # https://pythonprogramminglanguage.com/flask-hello-world/
    # reserved port numbers
    # https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
    app.run(host='0.0.0.0', port=50092)
    
    # Note for deployment:
    # http://flask.pocoo.org/docs/1.0/deploying/#deployment        