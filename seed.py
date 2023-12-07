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
    image_url='https://imgs.search.brave.com/1BB3_2WnMqvSSAPX5xlHPqGXQuK_Bxea-psX6zerqaE/rs:fit:860:0:[…]W51UTh3alFH/cmFUUlFtRlNZalkt/dldCcndnTm9hVEFG/bDhoeTRBUWM9'
)

db.session.add(matt)
db.session.add(giraffe)
db.session.add(fluffy)

db.session.commit()

