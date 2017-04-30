#!/usr/bin/python

import json
import csv
import sys
from pprint import pprint

if len(sys.argv) != 2:
    print("python wrapper.py <\"business name\">")
    exit(1)

def main():

    # Opening the food sentiment json file for data processing
    with open('data/food_sentiment.json') as data_file:    
        data = json.load(data_file)
    
    # opening and creating business dictionary corresponding to the business id
    businessDict = dict()
    with open('data/business_SC_name.csv') as file:
        dataReader = csv.DictReader(file)
        for i in dataReader:
            businessDict[i['name']] = i['business_id']
    
    # fetching the business name passed in the command line
    name = str(sys.argv[1])
    print('Restaurant: ', name)
    print('\nRecommended Food Items: \n')
    index = 1
    
    # fetching food items and printing the topmost food items in the list
    for items in data[businessDict[name]]['food_items']:
            food = data[businessDict[name]]['food_items'][items]
            if food['pos_count'] > 1:
                print(index, items)
                index += 1

if __name__ == '__main__':
    main()