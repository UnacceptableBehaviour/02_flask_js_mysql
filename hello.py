from flask import Flask, render_template, request
app = Flask(__name__)

from helpers import get_csv_from_server_as_disctionary, get_recipe_details



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

    url_file = 'http://192.168.0.8:8000/static/sql_recipe_data.csv'
    
    sql_dict = get_csv_from_server_as_disctionary(url_file)
    
    print(sql_dict.__class__.__name__)
    
    print(f">---------------------------------------- DICTIONARY LOADED >")
    
    for k, v in sql_dict.items():
        print(f"> > > K:{k} - V:{v['title']} {k.__class__.__name__}")
    
    #info = get_nutrients_per_serving()    
    info = {
        'image': '20190228_163410_monkfish and red pepper skewers.jpg',
        'n_Al': '0.0',
        'n_Ca': '3.46',
        'n_En': '108',
        'n_Fa': '3.85',
        'n_Fb': '1.27',
        'n_Fm': '1.43',
        'n_Fo3': '0.41',
        'n_Fp': '0.81',
        'n_Fs': '1.13',
        'n_Pr': '14.21',
        'n_Sa': '0.82',
        'n_St': '0.0',
        'n_Su': '2.17',
        'rcp_id': '23',
        'serving_size': '80',
        'text_file': '20190228_163410_monkfish and red pepper skewers.txt',
        'recipe_title': 'monkfish and red pepper skewers'
    }
    
    info = sql_dict[23]
    
    get_recipe_details(info['text_file'])
    
    headline_py = f"Recipe Page"
        
    return render_template("recipe_page.html", headline=headline_py, info=info, image_dict=sql_dict)
