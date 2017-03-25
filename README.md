# Yelp-Dataset-Challenge
This project is based on the Yelp Dataset Challenge where we are trying to solve one Business problem as part of the Business Intelligence.

**Problem: Based on User Reviews, which food item to suggest to a new user for a Restaurant**

**Dataset format in JSON for the project**
* yelp_academic_dataset_business.json
{
    "business_id":"encrypted business id",
    "name":"business name",
    "neighborhood":"hood name",
    "address":"full address",
    "city":"city",
    "state":"state -- if applicable --",
    "postal code":"postal code",
    "latitude":latitude,
    "longitude":longitude,
    "stars":star rating, rounded to half-stars,
    "review_count":number of reviews,
    "is_open":0/1 (closed/open),
    "attributes":["an array of strings: each array element is an attribute"],
    "categories":["an array of strings of business categories"],
    "hours":["an array of strings of business hours"],
    "type": "business"
}

* yelp_academic_dataset_review.json
{
    "review_id":"encrypted review id",
    "user_id":"encrypted user id",
    "business_id":"encrypted business id",
    "stars":star rating, rounded to half-stars,
    "date":"date formatted like 2009-12-19",
    "text":"review text",
    "useful":number of useful votes received,
    "funny":number of funny votes received,
    "cool": number of cool review votes received,
    "type": "review"
}




* yelp_academic_dataset_user.json
{
    "user_id":"encrypted user id",
    "name":"first name",
    "review_count":number of reviews,
    "yelping_since": date formatted like "2009-12-19",
    "friends":["an array of encrypted ids of friends"],
    "useful":"number of useful votes sent by the user",
    "funny":"number of funny votes sent by the user",
    "cool":"number of cool votes sent by the user",
    "fans":"number of fans the user has",
    "elite":["an array of years the user was elite"],
    "average_stars":floating point average like 4.31,
    "compliment_hot":number of hot compliments received by the user,
    "compliment_more":number of more compliments received by the user,
    "compliment_profile": number of profile compliments received by the user,
    "compliment_cute": number of cute compliments received by the user,
    "compliment_list": number of list compliments received by the user,
    "compliment_note": number of note compliments received by the user,
    "compliment_plain": number of plain compliments received by the user,
    "compliment_cool": number of cool compliments received by the user,
    "compliment_funny": number of funny compliments received by the user,
    "compliment_writer": number of writer compliments received by the user,
    "compliment_photos": number of photo compliments received by the user,
    "type":"user"
}

* yelp_academic_dataset_tip.json
{
    "text":"text of the tip",
    "date":"date formatted like 2009-12-19",
    "likes":compliment count,
    "business_id":"encrypted business id",
    "user_id":"encrypted user id",
    "type":"tip"
}

**Important Attributes in each Dataset related to project**
* Business Dataset
Business ID, Review Count, Open or Close, Stars, Name, 

* Review Dataset
User ID, Review ID, Business ID (to get Business Type, Stars, Review count and location), useful, cool.

* User Dataset
User ID, Elite, yelping_since, name, review_count, friends, fan, useful, cool.

* Tip Dataset
Text, likes, business id, user_id, type

**Related Research Paper**
https://pdfs.semanticscholar.org/8b2b/ada22181916196116f1711d456ea212f2b3b.pdf
https://link.springer.com/chapter/10.1007/978-3-319-08786-3_6
http://www.aclweb.org/anthology/P/P13/P13-2.pdf#page=547

* Important papers: http://dl.acm.org/citation.cfm?id=2631784
* Important papers: http://ltrc.iiit.ac.in/icon2015/icon2015_proceedings/PDF/54_rp.pdf




