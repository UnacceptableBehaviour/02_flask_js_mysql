from flask import Flask, render_template, request
app = Flask(__name__)


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
