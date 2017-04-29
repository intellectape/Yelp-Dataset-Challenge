#!/usr/bin/python

import pandas as pd
import jsonpickle

def load_wordlist(filename):
    return list(set([line.replace("\n", "") for line in open(filename, "r")]))

class Food:
    name = None
    pos_reviews = None
    neg_reviews = None
    pos_count = 0
    neg_count = 0


class Restaurant:
    buisness_id = -1
    food_items = None

def check_positivity(text):
    pos_count = 0
    neg_count = 0

    for word in positives:
        if word in text:
            pos_count += 1

    for word in negatives:
        if word in text:
            neg_count += 1

    if pos_count>=neg_count:
        return 1
    else:
        return -1




dataset = pd.read_csv("./Data/cleanedSC.csv")
positives = load_wordlist("positive.txt")
negatives = load_wordlist("negative.txt")

restaurant_dict = dict()

total_items = dataset["business_id"].__len__()

for i in range(0, total_items):
    business_id = dataset["business_id"][i]
    food_name = dataset["field1"][i]
    text = dataset["text"][i]
    rating = dataset["stars"][i]

    if business_id in restaurant_dict:
        restaurant = restaurant_dict.get(business_id)
        if food_name in restaurant.food_items:
            food = restaurant.food_items.get(food_name)
        else:
            food = Food()
            food.name = food_name
            food.pos_reviews = []
            food.neg_reviews = []
            food.pos_count = 0
            food.neg_count = 0
    else:
        restaurant = Restaurant()
        restaurant.buisness_id = business_id
        restaurant.food_items = dict()
        food = Food()
        food.name = food_name
        food.pos_reviews = []
        food.neg_reviews = []
        food.pos_count = 0
        food.neg_count = 0

    if int(rating) == 5:
        result = 1
    elif int(rating) == 1:
        result = -1
    else:
        result = check_positivity(text)

    if result > 0:
        food.pos_count += 1
        food.pos_reviews.append(text)
    elif result < 0:
        food.neg_count += 1
        food.neg_reviews.append(text)

    restaurant.food_items[food_name] = food
    restaurant_dict[business_id] = restaurant
    None

final_data = jsonpickle.encode(restaurant_dict, unpicklable=False)
final_file = open("final_data.txt", "w")
final_file.write(final_data)
final_file.close()
None


