import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Result

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config.from_object(os.environ.get['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return "Hello World!"
    return '<h1>Hello User</h1>'


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
