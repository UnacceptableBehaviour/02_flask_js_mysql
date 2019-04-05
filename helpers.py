#! /usr/bin/env python

# helper functions

import csv
import itertools
import re
from pathlib import Path

from pprint import pprint # giza a look

# serve files from http://192.168.0.8:8000/static/sql_recipe_data.csv
# $ cd /a_syllabus/lang/python/repos/assest_server 
# $ http-server -p 8000 --cors 
import urllib.request
# urllib.request.urlretrieve ("http://192.168.0.8:8000/static/sql_recipe_data.csv", "sql_recipe_data.csv")
# url = urllib.parse.quote(url, safe='/:')  # make sure files w/ spaces OK

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# load a csv file into a list of dictionaries
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def get_csv_from_server_as_disctionary(url):    
    print("----- get_csv_from_server_as_disctionary -----------------------------------")
    
    url = urllib.parse.quote(url, safe='/:')  # replace spaces if there are any - urlencode
    print(url)
    
    csv_file = url.split('/')[-1]
    
    print(csv_file)
    
    local_file_name = f"./scratch/{csv_file}"

    urllib.request.urlretrieve(url, local_file_name)

    sql_dict = {}

    with open(local_file_name) as csv_to_sql_file:    
        csv_reader = csv.DictReader(csv_to_sql_file, delimiter=',')    
        
        entry = {}
    
        entries = 0
        
        for row in csv_reader:
            entry = {}                          # create a new dictionary for each entry
            
            for col_key in csv_reader.fieldnames:                
                entry[col_key] = row[col_key]   # create and info dictionary    
    
            sql_dict[entries] = entry
            
            entries +=1

    pprint(sql_dict[23])
    
    print("----- reponse ------------------------------------------------------------")
    
    return sql_dict
    



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# load a text file from server - convert into partial recipe dictionary
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def get_recipe_details(recipe_text_filename):    
    recipe_info = {}
    
    print("----- get_recipe_details -------------------------------------------------")
    base_url = 'http://192.168.0.8:8000/static/recipe/'
    url = f"{base_url}{recipe_text_filename}"
    print(url)

    # IN  http://192.168.0.8:8000/static/recipe/20190228_163410_monkfish and red pepper skewers.txt
        
    #url = urllib.parse.quote(url)          # mangles name?
    # OUT http%3A//192.168.0.8%3A8000/static/recipe/20190228_163410_monkfish%20and%20red%20pepper%20skewers.txt
 
    #url = urllib.parse.quote_plus(url)          # mangles name? - 
    # OUT http%3A%2F%2F192.168.0.8%3A8000%2Fstatic%2Frecipe%2F20190228_163410_monkfish+and+red+pepper+skewers.txt 
    
    #url = url.replace(" ", "%20")          # WORKS 
    # OUT http://192.168.0.8:8000/static/recipe/20190228_163410_monkfish%20and%20red%20pepper%20skewers.txt

    #url = urllib.request.pathname2url(url)             # mangles name?
    # OUT http%3A//192.168.0.8%3A8000/static/recipe/20190228_163410_monkfish%20and%20red%20pepper%20skewers.txt
    
    #url = urllib.parse.quote(url, safe=':')            # partially mangles name . . 
    # OUT http:%2F%2F192.168.0.8:8000%2Fstatic%2Frecipe%2F20190228_163410_monkfish%20and%20red%20pepper%20skewers.txt
    
    url = urllib.parse.quote(url, safe='/:')  # WORKS 
    
    print(url)
    
    local_file_name = f"./scratch/{recipe_text_filename}"    
    print(local_file_name)

    ret_val = urllib.request.urlretrieve(url, local_file_name)    
    #pprint(ret_val)
    
    file_info  = Path(local_file_name)
    
    if file_info.is_file():
        print(f"File exists: {file_info}")
        f = open(local_file_name, 'r')              # load local file to work with
    else:
        print(f"File NOT PRESENT: {file_info}")
        return

    recipe_text = f.read()
    
    f.close()
    
    # Matches
    # 1 - name
    # 2 - portions
    # 3 - ingredients
    # 4 - yield
    match = re.search( r'^-+- for the (.*) \((\d+)\)(.*)^\s+Total \((.*?)\)', recipe_text, re.MULTILINE | re.DOTALL )
    
    recipe_info = {
        'recipe_title':"Initialised as NO MATCH",
        'ingredients':"Pure green",
        'portions': 0,
        'yield': '0g'
    }

    if (match):
        recipe_info['recipe_title'] = match.group(1).strip()
        recipe_info['portions'] = match.group(2).strip()
        recipe_info['yield'] = match.group(4).strip()
        i_list = (''.join( match.group(3).strip() ) ).split("\n")
        
        # remove comments (after #) from ingredients in recipe: 10g allspice     # woa that's gonna be strong!
        for index, line in enumerate(i_list):
            i_list[index] = ( re.sub('#.*', '', line) ).strip()
            
        
        for index, line in enumerate(i_list):                
            i_list[index] = list( filter(None, line.split("\t")) )
        
        
        print(f"NAME: {match.group(1).strip()}")
        print(f"PORTIONS: ({match.group(2).strip()})")
        print(f"INGREDIENTS:\n") #{match.group(3).strip()}")
        pprint(i_list)
        print(f"YIELD: {match.group(4).strip()}")
        
        #ingredients = [('46g','yellow cake uranium'),('1bag', 'plutoneum pellets'),('1list','secret codes'),('1sphere','blast concentrator')] # build an array of tuple to pass back in recipe_info
        #recipe_info['ingredients'] = ingredients
        recipe_info['ingredients'] = i_list
    else:
        print(f"BAD TEMPLATE IN {recipe_text_filename} < - = - = - = - = - = - = - = - = - = - = < < !!")
        # raise exception here
    
    return recipe_info

    
    
    
if __name__ == '__main__':
    print("-----  get CSV ------------------------------------S")
    fetch_file = 'http://192.168.0.8:8000/static/sql_recipe_data.csv'
    get_csv_from_server_as_disctionary(fetch_file)
    print("-----  get CSV ------------------------------------E")

    recipe_text = '20190228_163410_monkfish and red pepper skewers.txt'
    #recipe_text = '20190109_143622_crabcakes.txt'
    #urllib.request = 'http://192.168.0.8:8000/static/recipe/20190109_143622_crabcakes.txt'
    get_recipe_details(recipe_text)