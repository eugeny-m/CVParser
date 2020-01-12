# CVParser web application

This is a test challenge for DrwinTech interviewing process.  
The application extract skills from uploaded CV.  
Supported file formats: pdf, doc, docx  

Temporary deployed on: `https://drwin-tech-cvparser.herokuapp.com`

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python 3.8.1

### Installing

* get project files from github  
`git clone https://github.com/eugeny-m/CVParser.git`  
`cd CVParser`
* create python environment  
`python3.8 -m venv venv`
* activate venv  
`source venv/bin/activate`
* install packages  
`pip install -r requirements.txt`
* download nltk packages  
`python -m nltk.downloader words`  
`python -m nltk.downloader stopwords`
* create tables  
`python manage.py migrate`
* collect project static  
`python manage.py collectstatic`
* run server on 127.0.0.1:8000  
`python manage.py runserver`

## Deployment

Application has config for deploying on heroku server.  
Just create account and app on `https://dashboard.heroku.com/apps`  
and deploy with heroku git `https://devcenter.heroku.com/articles/git`

## Built With

* [Python 3.8.1](https://www.python.org)
* [Django 3.0.2](https://www.djangoproject.com) - The web framework used
* [Spacy 2.2.3](https://spacy.io)
* [nltk 3.4.5](https://www.nltk.org)

## Authors

* **Eugeny Maksimov** -  [eugeny-m](https://github.com/eugeny-m)  
* Great thanks to project [PyResparser](https://github.com/OmkarPathak/pyresparser).
It was taken as base for skills extractor
