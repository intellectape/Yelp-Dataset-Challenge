# Yelp-Dataset-Challenge
This project is based on the Yelp Dataset Challenge where we are trying to solve one Business problem as part of the Business Intelligence.

**Problem: Based on User Reviews, which food item to suggest to a new user for a Restaurant**

**Dataset format in JSON for the project**

* yelp_academic_dataset_business.json

{

    "business_id":"encrypted business id",
    
    "name":"business name",
    
    "stars":star rating, rounded to half-stars,
    
    "review_count":number of reviews,
    
    "is_open":0/1 (closed/open),
    
    "attributes":["an array of strings: each array element is an attribute"],
    
    "categories":["an array of strings of business categories"],
    
    "type": "business"
}

* yelp_academic_dataset_review.json

{

    "review_id":"encrypted review id",
    
    "user_id":"encrypted user id",
    
    "business_id":"encrypted business id",
    
    "stars":star rating, rounded to half-stars,
    
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
    
    "average_stars":floating point average like 4.31,
    
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

* Business Dataset: Business ID, Review Count, Open or Close, Stars, Name, 

* Review Dataset: User ID, Review ID, Business ID (to get Business Type, Stars, Review count and location), useful, cool.

* User Dataset: User ID, Elite, yelping_since, name, review_count, friends, fan, useful, cool.

* Tip Dataset: Text, likes, business id, user_id, type


**Related Research Paper**

* https://pdfs.semanticscholar.org/8b2b/ada22181916196116f1711d456ea212f2b3b.pdf

* https://link.springer.com/chapter/10.1007/978-3-319-08786-3_6

* http://www.aclweb.org/anthology/P/P13/P13-2.pdf#page=547

* Important papers: http://dl.acm.org/citation.cfm?id=2631784
* Important papers: http://ltrc.iiit.ac.in/icon2015/icon2015_proceedings/PDF/54_rp.pdf
