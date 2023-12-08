"""Models for Blogly."""

print("***** MODELS.PY   ")
from flask_sqlalchemy import SQLAlchemy
from time import ctime

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://img.freepik.com/premium-vector/"\
    "3d-realistic-person-people-vector-illustration_156780-246.jpg?w=826"

def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)

class User(db.Model):
    """ User class that includes an id as primary key, first name, last name
    and profile image url. """

    __tablename__= "users"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    first_name = db.Column(
        db.String(50),
        nullable=False
        )

    last_name = db.Column(
        db.String(50),
        nullable=False
    )

    image_url = db.Column(
        db.Text,
        nullable=False,
        default=DEFAULT_IMAGE_URL
    )


class Post(db.Model):
    """ A class for blog post, it includes primary key, title, content,
    as well as date and time when post is created"""

    __tablename__="posts"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    title = db.Column(
        db.Text,
        nullable=False
    )

    content = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=ctime()
    )