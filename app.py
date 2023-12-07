"""Blogly application."""

import os

from flask import Flask, request, redirect, render_template, flash
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
def homepage():
    """Show homepage with current list of user """

    return redirect("/users")

@app.get("/users")
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

    return redirect('/users')

@app.get("/users/<int:user_id>")
def show_user_info(user_id):
    """Show info on a single user."""

    user = User.query.get_or_404(user_id)
    return render_template("user-info.html", user=user)

@app.get("/users/<int:user_id>/edit")
def show_edit_form(user_id):
    """Show the edit form with user's information in inputs."""

    user = User.query.get(user_id)
    return render_template("edit.html", user=user)

@app.post("/users/<int:user_id>/edit")
def handle_edit_form(user_id):
    """Retrieve information from inputs, update the database,
    and redirect user back to /users page"""

    user = User.query.get(user_id)

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url'] if request.form['image_url'] else None

    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url

    db.session.add(user)
    db.session.commit()

    return redirect('/users')


@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):
    """ Delete a user from the users table and from the homepage list.
    This function is primarily accessed via the user form at users/#/edit. """

    user = User.query.get(user_id)

    db.session.delete(user)
    db.session.commit()

    flash(f"User {user.first_name} {user.last_name} has been terminated.")
    return redirect('/users')







