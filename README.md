# Twitter Python Tips

Have you ever heard of Daily Python Tip? It's a Twitter account that posts one python tip per day, run by @karlafej and @simecek.

This is a simple web app made with django to get tweets from the @python_tip twitter page, and provides search capabilities to
help navigate through tweets.
You can get al setup in just few steps.

- create a virtual environment and install packages from requirements.txt
- create an app on twitter and get the consumer key, consumer secret, access token, 
and access token secret.
- save each of them in a ```.env```  file on the root folder with the names 
```CONSUMER_KEY```, ```CONSUMER_SECRET```, ```ACCESS_TOKEN``` and ```ACCESS_TOKEN_SECRET```
respectively.
- On two different terminals run the following commands to start celery; 
```celery -A twitter_python_tips beat -l info```, and
 ```celery -A twitter_python_tips worker -l info```. To populate the database with 
 tips
- You could also populate the database from twitter by running the following command 
```python manage.py grab_tweets``` with the optional ```-c``` and ```-t``` arguments
to set count and twitter id.
- Start your server ```python manage.py runserver``` and you are all set up.
