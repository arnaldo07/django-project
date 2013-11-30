## django-project-template

django-project-template is a Django 1.6+ project template, giving you a skeleton web application with some useful, but general, features. 

### Features

+ Environment variable based database configuration
    + [dj-database-url](https://github.com/kennethreitz/dj-database-url) configures the database from the DATABASE_URL env var.
    + database passwords kept in environment variables and out of source.
    + integrates with Amazon RDS, Heroku DBs, and others easily.
+ Separate development, staging, and production environments.
    + keeps projects organized and aids in debugging
    + switch environments easily based on APP_ENV env var.
    + separate settings per environment on top of base settings.
    + separate requirements per environment on top of base requirements.
+ S3 static resource collection and hosting integrations.
+ Deployable directly to Heroku.
+ Helps your construct web applications that follow the [12factor](http://12factor.net/) methodology.

### Usage

Create a virtual environment in which to install Django and other pip packages. See [virtualenv](https://pypi.python.org/pypi/virtualenv) or [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/))

    workon django-myproj  # activate a virtualenvwrapper virtualenv
    pip install django

If you have git cloned [django-project-template](https://github.com/dghubble/django-project-template),

    django-admin.py startproject --template=/path/to/django-project-template --extension py,md myproj

otherwise,

    django-admin.py startproject \
    --template=https://github.com/dghubble/django-project-template/zipball/master \
    --extension py,md myproj

A *myproj* project directory containing a README.md, a manage.py script, and a *myproj* Python package directory was created. Rename the outer (project) directory to anything you wish, but don't modify the inner (package) directory or package name.

    mv myproj convenient-name   # optional

Navigate into the project directory. For all of the remaining instructions, you should be located inside the project directory.

#### Select Project Database

django-project-template encourages use of MySQL or PostgreSQL in development, for greater parity with the staging and production environments. Install and configure either MySQL([guide]()) or PostgreSQL([guide]()) on your local machine if you have not already done so. In your project's README.md file, under `Machine Prep`, remove the line about MySQL or PostgreSQL, whichever your project does not use.

Open the settings.py file within your project package directory and uncomment one of the MySQL, PostgreSQL, or SQLite settings sections within DATABASES. Check that the default database url string (e.g. mysql://username:password@localhost:3306/django_myproj) has the correct scheme, username, password, port, and database name.

django-project-template allows storing local database authentication credentials in source code since in development environments, throw-away database accounts and databases are frequently used. However, if this is a concern, remove the default keyword argument to `dj_database_url.config` entirely so the database used by the Django project is configured by the DATABASE_URL environment variable alone.

### Continuing

The django-project-template README is divided into 2 parts. The first, which includes this and prior sections, describes how to generate a Django project from the template. The later part is a skeleton for the README of your generated project - it is personalized for your project so instead of {% project_name %} blocks, your project name will be used instead. 

If you haven't already, switch to the README.md file generated inside your personal Django project and continue following the directions there, from this point. 

Once you develop your project a little further, you may delete the first part of this README so it can focus on describing your Django project, shwoing how to setup the project, etc. 


## proj Project

### Overview

proj ...

### Machine Prep

If you haven't already, install and configure MySQL on your local machine ([guide]()). 
If you haven't already, install and configure PostgreSQL on your local machine ([guide]()). 

Create a database user and database django_proj to use for proj development. Ensure the database url string under DATABASES in proj/settings.py corresponds to your setup.

### Project Setup

Create a virtual environment in which to install Python pip packages. Virtual environment activation with [virtualenv](https://pypi.python.org/pypi/virtualenv),

    virtualenv venv            # create virtualenv venv
    source venv/bin/activate   # activate 

or with [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/),

    mkvirtualenv django-myproj # create and activate environment
    workon django-myproj       # reactivate existing environment

Now, check requirements/development.txt and comment/uncomment Linux/OS X depending on your platform. Install development dependencies,

    pip install -r requirements/development.txt

Setup database tables,

    python manage.py syncdb    # create neccessary tables

Run the web application locally,

    python manage.py runserver # 127.0.0.1:8000


### Adding Apps

Projects templated from django-project-template are designed so that reusable apps you include source code for can be placed adjacent to the project's package directory proj. Add the (unprefixed) app names to proj/settings.py INSTALLED_APPS. The `static` and `templates` directories of your included apps should use inner directories that match the name of the app for namespacing.

Start creating included source reusable Django apps with

    python manage.py startapp appname

### Deployment

#### Heroku



