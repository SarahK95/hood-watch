## Project Title

### Awards

## Project Description
A web app that keeps you on the loop with the happenings in your neighbourhood.

### User story
- Sign up and log in
- Choose your neighbourhood
- View  posts 
- Post  posts
- Comment on a post
- Edit your profile
- See police and health


## Specifications
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| User visits the app and gets directed to the login page  | User logs in | Directed to the home page | 
If user has no account, they click on `sign up` | User signs up | User is redirected to the profile set up page |
| Homepage loads | Click ` Posts` | User's redirected to a page where they can see uploaded posts and a button to post too | 
| Homepage loads | Click `Health ` | User's redirected to a page where they can see health services | 
| Homepage loads | Click `Businesses` | User's redirected to a page where they can see uploaded businesses |
| Homepage loads | Click `Police` | User's redirected to a page where they can see posted police in the same neighbourhood |
| Homepage loads | User inputs in the search form and presses enter | Searched results show |


## Installing

- Copy this ![link]https://github.com/SarahK95/hood-watch.git
- Clone the repo to your terminal
- Run the code on a virtual enviroment and also have django installed
- For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
- To run the app, you'll have to run the following commands in your terminal

       pip install -r requirements.txt
1. On your terminal,Create database gallery using the command below.


       CREATE DATABASE db-name
2. Migrate the database using the command below


       python3.8 manage.py migrate
3. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


       python manage.py runserver
4. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

## Prerequisites

- Python3
- Django
- virtual environment


## Deployment
- log in to heroku
```
heroku login
```
- create heroku app
```
heroku create app
```
- Upload requirements
```
pip freeze
```
- create a postgres addon to your heroku app
```
heroku addons:create heroku-postgresql:hobby-dev
```
- push to heroku

```
git push heroku master
```
- run migrations
```
heroku run python manage.py migrate
```

## Licence
- MIT License
- Copyright (c) 2022 Sarah Kamunya
