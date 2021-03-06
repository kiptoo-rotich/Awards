#  AWARDS

#### Author: [Kiptoo Rotich](https://github.com/kiptoo-rotich)

## Screenshot
### Landing page
![home page](https://user-images.githubusercontent.com/48821300/126333113-d08e945f-921b-4242-acf8-ca82375bc6d1.png)

### Profile
![profile](https://user-images.githubusercontent.com/48821300/126333273-618dfb3e-28e7-48f9-a4b5-ecff4f093836.png)

### Reviews
![reviews](https://user-images.githubusercontent.com/48821300/126333371-97b5957b-c4b2-4d1f-b50a-d5657364df8b.png)

### Search results
![search](https://user-images.githubusercontent.com/48821300/126333460-69166654-932b-47a9-8fc8-f8413c56f655.png)


## Description
The application allows users to post their projects by descripting what the project is about, the title, the technologies used and a screen shot of the subject. Moreover, viewers can review the project and also give a rating.

As a user of the web application you will be able to:

1. Sign up and log in
2. Post projects
3. View posted projects
4. Rate a project
5. Edit your profile
6. Consume API
7. Review project


## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.8 manage.py runserver`
* Access the live site using the local host provided
* Create your superuser account `python manage.py createsuperuser` inside virtual environment.
* Add data from admin dashboard

## End points
```bash
https://awards27.herokuapp.com/api/projects/
```

## Getting started

### Prerequisites
* python3.8
* virtual environment
* pip
* postgresql
  

#### Clone the Repo and rename it to suit your needs.
```bash
git clone `https://github.com/kiptoo-rotich/Awards`
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.8 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'your secret key'
DEBUG=True
DB_NAME='gallery'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.8 manage.py check
python manage.py makemigrations news
python3.8 manage.py sqlmigrate news 0001
python3.8 manage.py migrate
```

#### Run the app
```bash
python3.8 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test projects`
        
## Built With

* [Python3.8](https://docs.python.org/3/)
* Django==3.2.5
* Postgresql 
* Boostrap
* HTML
* CSS


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license)