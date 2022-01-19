# Guide
This guide is for Mac OS. I worked on this on a macbook and have not had the chance to work on Windows/Linux to figure out the proper setup instructions.
To get started you need to install Python 3. Once you have Python 3 installed you will need to install a couple of other dependencies.

Clone the project
```
$ git clone https://github.com/Jami159/shopify_project.git
```

## Install local MySQL server

You will need to install `mysql` on your computer to use as the database for the CRUD operations for this web app.
We could hook up our app to any MySQL database, but this is the easiest setup (that I could think of) for this project.

(This assumes you have `homebrew` installed (if not, it's fairly easy to set up - pls google).
 ```
 $ brew install mysql
 ```

Once `mysql` is installed you need to start and setup a local database that the web app can communicate with
```
$ mysql.server start
$ mysql -u root
```

Then in the `mysql` shell
```
mysql> CREATE USER 'shopify_admin'@'localhost' IDENTIFIED BY 'shopify_challenge';
mysql> CREATE DATABASE shopify_db;
mysql> GRANT ALL PRIVILEGES ON shopify_db . * TO 'shopify_admin'@'localhost';
```

## virtualenv
Open up a new terminal - we want to keep our sql server up and running.
The following steps will be all in the new terminal.

Install `virtualenv`
 ```
 $ pip3 install virtualenv
 ```
Once `virtualenv` is installed, create a new `virtualenv`
 ```
 $ virtualenv shopify_env
 ```
 Then activate it
 ```
 $ source shopify_env/bin/activate
 ```
Then go into your project directory and install project dependencies
 ```
 $ cd shopify_project
 $ pip3 install -r requirements.txt
 ```

## Environment variables

You need to setup a couple environment variables that the web app will use
```
$ export FLASK_CONFIG=development
$ export FLASK_APP=run.py
```

## Create table in MySQL database
This table will be created from the table definition in `shopify_project/app/models.py`
```
$ flask db init
$ flask db migrate
$ flask db upgrade
```

## Run the app
```
$ flask run

* Serving Flask app "run"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

On your browser go to `http://127.0.0.1:5000/`

You should see a basic web page with all the CRUD functionallity as well as an `Export CSV` button for the additional funtionality for this challenge.

# Have fun!
