print("***** TESTS.PY")
import os

os.environ["DATABASE_URL"] = "postgresql:///blogly_test"

from unittest import TestCase

from app import app, db
from models import User   # DEFAULT_IMAGE_URL,

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.drop_all()
db.create_all()


class UserViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client, add sample data."""

        # As you add more models later in the exercise, you'll want to delete
        # all of their records before each test just as we're doing with the
        # User model below.
        User.query.delete()

        test_user = User(
            first_name="test1_first",
            last_name="test1_last",
            image_url=None,
        )

        db.session.add(test_user)
        db.session.commit()

        # We can hold onto our test_user's id by attaching it to self (which is
        # accessible throughout this test class). This way, we'll be able to
        # rely on this user in our tests without needing to know the numeric
        # value of their id, since it will change each time our tests are run.
        self.user_id = test_user.id

    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as c:
            resp = c.get("/users")
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn("test1_first", html)
            self.assertIn("test1_last", html)


    ### Additional tests below ###

    def test_show_new_user_form(self):
        with app.test_client() as c:
            resp = c.get('/users/new')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Create a user", html)


    def test_create_user(self):
        with app.test_client() as c:
            resp = c.post('/users/new',
                           data={'first_name': 'test2_first',
                                  'last_name': 'test2_last',
                                  'image_url': 'None'}, follow_redirects=True)
            html = resp.get_data(as_text=True)
            # Change image_url to '' insteaad of None

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(   # Set the query to a variable to help formatting
                'test2_first',
                User.query.filter(
                    User.first_name == 'test2_first'
                ).one().first_name)
            self.assertIn('test2_first test2_last', html)


    def test_show_edit_form(self):
        with app.test_client() as c:
            resp = c.get(f'/users/{self.user_id}/edit')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Edit a user", html)


    def test_delete_user(self):
        with app.test_client() as c:
            resp = c.post(f'/users/{self.user_id}/delete',
                          data={'id': self.user_id}, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIsNone(User.query.filter(
                User.id == self.user_id).one_or_none())
            self.assertIn('test1_first test1_last has been terminated', html)
            # (yes, keep the literal string of what was expectecd.)





