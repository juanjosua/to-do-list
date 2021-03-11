from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

from project.todos.views import todos_blueprint
app.register_blueprint(todos_blueprint, url_prefix='/todos')


@app.route('/')
def root():
    return redirect(url_for('todos.index'))
