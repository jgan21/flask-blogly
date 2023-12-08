from models import db, User
from app import app

db.drop_all()
db.create_all()

# Add users
matt = User(
    first_name='Matt',
    last_name='Smida',
    image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyPymeYqn2wOD8j-kLZZFjCHkHOHaOZ0nTFKVXlHQMqgDe8T1a')

giraffe = User(
    first_name='Longe',
    last_name='Necke',
    image_url='https://m4t7.net/images/matt.jpg'
)

fluffy = User(
    first_name='Fluffy',
    last_name='Burton',
)

db.session.add(matt)
db.session.add(giraffe)
db.session.add(fluffy)

db.session.commit()

