# django-project-template

django-project-template is a Django 1.6+ project template, giving you a skeleton web application with some useful, but general, features. 

## Features

+ Separate dev, stag, and prod environments.
    + cleanly separates settings and requirements
    + switch environments easily based on APP_ENV env var.
+ [django-storages](http://django-storages.readthedocs.org/en/latest/) static asset storage backend integration with S3.
+ Environment variable based database configuration
    + [dj-database-url](https://github.com/kennethreitz/dj-database-url) configures the database from the DATABASE_URL env var.
    + database passwords kept in environment variables and out of source.
    + integrates with Amazon RDS, Heroku DBs, and others easily.
+ Deployable directly to Heroku.
+ Helps you construct organized web applications that follow the [12factor](http://12factor.net/) methodology.
+ Default project 404 and 500 error pages. 

## Usage

Create a virtual environment in which to install Django and other pip packages. See [virtualenv](https://pypi.python.org/pypi/virtualenv) or [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/))

    workon django-myproj  # activate a virtualenvwrapper virtualenv
    pip install django

If you have git cloned [django-project-template](https://github.com/dghubble/django-project-template),

    django-admin.py startproject \
    --template /path/to/django-project-template \
    -e py,md,html \
    -n Procfile myproj

otherwise,

    django-admin.py startproject \
    --template https://github.com/dghubble/django-project-template/zipball/master \
    -e py,md,html \
    -n Procfile myproj

A *myproj* project directory containing a README.md, a manage.py script, and a *myproj* Python package directory was created. Rename the outer (project) directory to anything you wish, but don't modify the inner (package) directory or package name.

    mv myproj convenient-name   # optional

If you specified an output path after *myproj* in the template command, the project directory *contents* will be placed at that location, not within a project directory.

Navigate into the directory containing the project. For all of the remaining instructions, you should be located inside the project directory.

### Database Type

django-project-template encourages use of MySQL or PostgreSQL in development, for greater parity with the staging and production environments. Install and configure either MySQL([guide]()) or PostgreSQL([guide]()) on your local machine if you have not already done so. Next remove requirements that are commented with databases you are not using. Also, in your project's README.md file, under `Prerequisites`, remove mention of any databases you are not using.

Open the settings.py file within your project package directory and uncomment one of the MySQL, PostgreSQL, or SQLite settings sections within DATABASES. Check that the default database url string has the correct scheme, username, password, port, and database name.

django-project-template allows storing local database authentication credentials in source code since in development environments, throw-away database accounts and databases are frequently used. However, if this is a concern, remove the default keyword argument to `dj_database_url.config` entirely so the database used by the Django project is configured by the DATABASE_URL environment variable alone.

## Going Further

The django-project-template README is divided into 2 parts. The first is django-project-template specific and describes how to generate a Django project from the template. The second part begins with the heading "proj Project" and serves as a skeleton README of the generated project - it is personalized for your project so instead of {% project_name %} blocks, your project name will be used instead. 

If you haven't already, switch to the README.md file generated inside your personal Django project and continue following the directions there, from this point. 

Once you develop your project a little further, you may delete the first part of this README so it focuses on your Django Project, its setup, etc. 

## Contributing

Want a particular feature? Discovered a bug or problem? Open an issue. Here are some nice [Issue Guidelines](https://github.com/necolas/issue-guidelines/blob/master/CONTRIBUTING.md) you can follow. 



# proj Project

## Overview

proj a Django web application ...

... initially based on the [django-project-template](https://github.com/dghubble/django-project-template).

## Prerequisites

If you haven't already, install and configure MySQL on your local machine ([guide]()). 
If you haven't already, install and configure PostgreSQL on your local machine ([guide]()). 

Create a database user and database django_proj to use for proj development. Ensure the database url string under DATABASES in proj/settings.py corresponds to your setup.

## Setup

Create a virtual environment in which to install Python pip packages. Virtual environment activation with [virtualenv](https://pypi.python.org/pypi/virtualenv),

    virtualenv venv            # create virtualenv venv
    source venv/bin/activate   # activate 

or with [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/),

    mkvirtualenv django-myproj # create and activate environment
    workon django-myproj       # reactivate existing environment

Install development dependencies,

    pip install -r requirements/development.txt

Setup database tables,

    python manage.py syncdb    # create neccessary tables

Run the web application locally,

    python manage.py runserver # 127.0.0.1:8000


## Workflow


### Environments

Switch environments by changing the value of the APP_ENV environment variable.

The `development` or `dev` environment runs the Django application with DEBUG set to true on a small development server which auto-reloads changed files. Django trackbacks are shown instead of error pages. Django itself serves the static assets located inside your project and apps. The database you have created on your local machine is used

The `staging` or `stag` environment can be run both locally or deployed because it includes both in ALLOWED_HOSTS. If deployed, the staging deployment should be separate from the production deployment (e.g. different Heroku application). The staging environment uses production type deployed static assets and databases though the actual hosted assets use a different S3 bucket from production and the staging database should be separate from the production database. Authentication keys or credentials are kept in environment variables, not in source.

Typically, when moving from `development` to `staging`, first switch to the staging environment locally and run the project with manage.py's runserver to test whether interactions with production type static assets and databases works without issue. Staging deployments should use production type webservers so that `staging` is identical to `production` except for the names of buckets, dbs, etc.

The `production` or `prod` environment is the environment in which your application should run in the real world. All authentication keys or credentials are kept in environment variables, not in source. The project should be served by a production quality webserver such as [gunicorn](http://gunicorn.org/). Static assets should be served from a a globally available file store (S3) or CDN. Production databases should be backed up and fortified. Production static asset stores and databases should be touched with extreme caution.


### Static Resources

In development, static assets are hosted at '<base_url>/static/' + namespacing appname + path to the asset within the 'myapp/static/myapp' directory. In your templates, include {% load staticfiles %} at the top of the template and reference static assets like,

    <img src="{% static 'appname/img/myimage.png' %}" alt="myimage">

proj uses the standard `django.contrib.staticfiles` app so in development, when the DEBUG setting is true, static assets are served automatically with runserver. 


### Deploying Static Resources

In staging and production environments, using a web process to serve static assets is not appropriate. proj uses `django-storages` adapters to upload collected static assets to Amazon S3 and to replace static template tags correctly.

First, create [S3 buckets](https://console.aws.amazon.com/s3) django_proj_static and django_proj_static_staging (set in proj/settings/staging.py and proj/settings/production.py) for static assets. Then create an [IAM](https://console.aws.amazon.com/iam/home) user django_proj with the Full S3 Access permission policy.

Be sure the APP_ENV, SECRET_KEY, AWS_ACCESS_KEY_ID, and AWS_SECRET_ACCESS_KEY environment variables are set in your environment.

Upload static files,

    python manage.py collectstatic  # when APP_ENV is staging or production

Then, in staging and production, the static assets uploaded to the staging and production buckets, respectively, will be referenced in your templates.

*Note: If a STATIC_ROOT directory was created in your project directory, your APP_ENV is set to development. Delete the STATIC_ROOT directory.*

### Adding Apps

Projects templated from django-project-template are designed so that reusable apps you include source code for can be placed adjacent to the project's package directory proj. Add the (unprefixed) app names to proj/settings.py INSTALLED_APPS. The `static` and `templates` directories of your included apps should use inner directories that match the name of the app for namespacing.

Start creating included source reusable Django apps with

    python manage.py startapp appname



## Deployment

Before you deploy, customize the ALLOWED_HOSTS in proj/settings/staging.py and proj/settings/production.py to match only your deployment domain.


### Heroku

Create Heroku app repo and add Git remote `heroku`,

    heroku login               # if you haven't already
    heroku create              # from within project directory
    
Now rename your project on Heroku,

    heroku apps:rename newname # dashes instead of underscores
    git remote -v              # should list 'heroku' as a remote repo

Define the following environment variables for the Heroku application:

+ APP_ENV
+ SECRET_KEY
+ AWS_ACCESS_KEY_ID
+ AWS_SECRET_ACCESS_KEY

as follows,

    heroku config:set APP_ENV=staging
    heroku config:set SECRET_KEY='random secret...'
    ...
    heroku config              # check env vars are correct

Turn on Heroku's `user-env-compile` feature so `django-storages` can read environment variables to determine how to collect and upload static assets.

    heroku labs:enable user-env-compile


#### Database Connection

##### MySQL

For MySQL, [setup]() your [Amazon RDS](https://console.aws.amazon.com/rds/home) instance, database user, and database. Be sure to require [SSL encrypted](http://aws.amazon.com/rds/faqs/#54) connections. Alternately, use another [supported](https://addons.heroku.com/?q=mysql) MySQL provider.

    heroku addons:add amazon_rds url=mysql2://user:pass@rdshostname.amazonaws.com:3306/dbname
    heroku config              # check DATABASE_URL is correct           

For conventience, add you MYSQL_HOST to an environment variable so you can connect to your database directly if needed.

    export MYSQL_HOST=dbidentifier.ch34mweifni.region-rds.amazonaws.com
    mysql -h $MYSQL_HOST -u master_user -p

##### PostgreSQL

For PostgreSQL, ...


#### Pushing

Push your application to Heroku,

    git push heroku master:master

One-off commands allow setting up database tables and uploading static assets as you would do locally. Heroku's `user-env-compile` lab should allow `django-storages` to automatically collect and upload static assets so the first command may not be needed.

    heroku run python manage.py collectstatic
    heroku run python manage.py syncdb

Check up on your Heroku application,

    heroku open                # open application in browser
    heroku ps                  # see web/worker counts and stats

#### Troubleshooting

    heroku ps
    heroku logs                # check Heroku logs
    heroku config              # check your Heroku env vars
    heroku restart             # restart dynos


### EC2













