import os
from unittest import TestCase
from models import db, connect_db, Message, User

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"
from app import app, CURR_USER_KEY

class UserViewTestCase(TestCase):
    def setUp(self):
        """Create test client, add sample data."""
        db.drop_all()
        db.create_all()
        self.client = app.test_client()

    def test_signup_user(self):
        """Can signup a user?"""
        testuser = User.signup(username="testuser",
                               email="test@test.com",
                               password="testuser",
                               image_url=None)
        db.session.commit()

        user = User.query.one()
        self.assertEqual(user.username, "testuser")