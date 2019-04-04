#! /usr/bin/env python

# helper functions

import csv
import itertools
import re

from pprint import pprint # giza a look

# serve files from http://192.168.0.8:8000/static/sql_recipe_data.csv
# $ cd /a_syllabus/lang/python/repos/assest_server 
# $ http-server -p 8000 --cors 
import urllib.request
# urllib.request.urlretrieve ("http://192.168.0.8:8000/static/sql_recipe_data.csv", "sql_recipe_data.csv")


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# load a csv file into a list of dictionaries
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def get_csv_from_server_as_disctionary(url):    
    print("----- get_csv_from_server_as_disctionary -----------------------------------")
    print(url)
    
    csv_file = url.split('/')[-1]
    
    print(csv_file)
    
    local_file_name = f"./scratch/{csv_file}"

    #urllib.request.urlretrieve (url, local_file_name)          << COMMENT BACK IN AND FAILS

    sql_dict = {}

    with open(local_file_name) as csv_to_sql_file:    
        csv_reader = csv.DictReader(csv_to_sql_file, delimiter=',')    
        
        entry = {}
    
        entries = 0
        
        for row in csv_reader:
            entry = {}                          # create a new dictionary for each entry
            
            for col_key in csv_reader.fieldnames:                
                entry[col_key] = row[col_key]   # create and info dictionary    
    
            #print(f"\n> > {entries}")
            #print(line)                        
            sql_dict[entries] = entry
            #print(f"\n> > {entries}")
            #print(sql_dict[entries])                        
            
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
        
    local_file_name = f"./scratch/{recipe_text_filename}"    
    
    #urllib.request.urlretrieve (url, local_file_name)          #<<<< ISSUE HERE

    f = open(local_file_name, 'r')              # copied over file to work with

    recipe_text = f.read()
    
    f.close()
    
    # Matches
    # 1 - name
    # 2 - portions
    # 3 - ingredients
    # 4 - yield
    match = re.search( r'^-+- for the (.*) \((\d+)\)(.*)^\s+Total \((.*?)\)', recipe_text, re.MULTILINE | re.DOTALL )
    
    #recipe_info['title'] = 'well no lets not be ruhing into anything ma boy'
    
    r_ingredients = match.group(3).strip()
    print(f"NAME: {match.group(1).strip()}")
    print(f"PORTIONS: ({match.group(2).strip()})")
    print(f"INGREDIENTS:\n{match.group(3).strip()}")
    print(f"YIELD: {match.group(4).strip()}")