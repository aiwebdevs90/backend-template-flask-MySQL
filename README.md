# Backend-Template-Flask-MySQL

Backend template using HTML5, CSS3, JavaScript, Flask and connected to a MySQL database.

* The first thing that needs to be done is update your VSCode packages, type the following command in the CLI:

`sudo apt update`

* Once that is done, now its time to install Postgresql and a contrib package which adds some additional utilities and functionality:

`sudo apt install postgresql postgresql-contrib`

* Now with postgresql installed you need to start the postgresql server:

`sudo service postgresql start`

* With the command you can also check the status of the status, or restart and stop the postgresql server:

```
sudo service postgresql status
sudo service postgresql restart
sudo service postgresql stop
```

* Now that the server has been started and everything has been installed, it created a default account called `postgres`, to access this account and to started creating database you need to type the following command:

`sudo -i -u postgres` or `sudo su postgres`

* Now you need to access the postgresql prompt and from here you can use various commands to create databases, tables, columns and more:

`psql`

* To create a database you need to type the following command:

`create database dbname;`

You can replace dbname with a database name of your choice.

* To delete a database you use the following command in the psql prompt:

`drop database dbname;`

* To view the new database created, type the following command in the psql prompt:

`\l`

* To view the users of database, type the following command in the psql prompt:

`\du`

* To exit the psql prompt, type the following command in the psql prompt:

`\q`

* To exit the postgres terminal, type the following command in the psql terminal:

`exit`

* To access or login back into postgresql, type the following command in the terminal:

`sudo -i -u postgres` or `sudo su postgres`

* To connect to your newly created database, type the following command in the psql prompt:

`\c dbname`

* Now exit out of the psql prompt by typing `\q` and then exit out of the postgresql prompt by typing `exit`
  
* Now install these python packages and typing in the following command in the terminal:

`pip3 install psycopg2 psycopg2-binary Flask-SQLAlchemy Flask-Migrate`

* Once the packages are installed, then freeze the requirements to text file:

`pip3 freeze --local > requirements.txt`

* The next file is the environment file to hide sensitive date, again can be done by right clicking on the file panel or type into the CLI:

`touch env.py`

* The next file that needs to be created is the .gitignore file, once a file is added to the ignore list it will not be pushed to github and the env.py needs to be added to this and never pushed to github for security reasons. Again can be done by right clicking on the file panel or type into the CLI:

`touch .gitignore`

* To add the env.py to the .gitignore list you can either manually type in the list when .gitnore file is opened:

```
env.py
__pycache__/ 
```

* Another method to add file to the .gitignore can be found in the changes section of VSCode and gitpod, you can right click on the file you want to ignore and click on the option to add to .gitignore

* Now its time to create a env.py file and enter the following code and make sure you add this to .gitignore:

```
import os

os.environ.setdefault("IP", "127.0.0.1") or ("IP", "0.0.0.0")
os.environ.setdefault("PORT", "8000") or ("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "go this address: https://randomkeygen.com/ and copy a random key, i chose fort knox passwords and paste here between the double quotes")
os.environ.setdefault("DATABASE_URL", "postgresql:///<dbname>")

Replace <dbname> with your database name that you created earlier
```

* Now its time to create a config.py file and enter the following code:

```
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
```