# CVParser web application

This is a test challenge for DrwinTech interviewing process.  
The application extract skills from uploaded CV.  
Supported file formats: pdf, doc, docx  

Just upload your file in fileinput on index page '/'  
and get responce with listed skills.

#### Built With:

* Python 3.8.1
* Django 3.0.2


#### Project run

* get project files from github
* `git clone https://github.com/eugeny-m/CVParser.git`
* `cd CVParser`
* create python environment
* `python3.8 -m venv venv`
* activate venv
* `source venv/bin/activate`
* install packages
* `pip install -r requirements.txt`
* download nltk packages
* `python -m nltk.downloader words`  
* `python -m nltk.downloader stopwords`
* create tables
* `python manage.py migrate`
* collect project static
* `python manage.py collectstatic`
* run server on 127.0.0.1:8000
* `python manage.py runserver`

