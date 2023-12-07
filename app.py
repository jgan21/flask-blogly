"""Blogly application."""

import os

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

@app.get("/")
def list_users():
    """List users' first and last name on the page"""

    users = User.query.all()
    return render_template("list.html", users=users)



@app.get("/users/new")
def show_new_user_form():
    """ Show new user form. """
    return render_template('new-user.html')

@app.post("/users/new")
def create_user():

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url'] if request.form['image_url'] else None

    new_person = User(
        first_name=first_name,
        last_name=last_name,
        image_url=image_url
        )

    db.session.add(new_person)
    db.session.commit()

    return redirect('/')
