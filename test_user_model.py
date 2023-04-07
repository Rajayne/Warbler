"""User model tests."""
# run these tests like:
#    python -m unittest test_user_model.py
import os
from unittest import TestCase
from models import db, User, Message, Follows

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"
from app import app, CURR_USER_KEY

db.drop_all()
db.create_all()
class UserModelTestCase(TestCase):
    def setUp(self):
        """Create test client, add sample data."""
        User.query.delete()
        Message.query.delete()
        Follows.query.delete()
        self.client = app.test_client()

    def test_user_model(self):
        """Does basic model work?"""
        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )
        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)

    def test_user_follow(self):
        u1 = User(
            email="user1@test.com",
            username="user1",
            password="HASHED_PASSWORD"
        )
        u2 = User(
            email="user2@test.com",
            username="user2",
            password="HASHED_PASSWORD"
        )
        db.session.add_all([u1, u2])
        db.session.commit()

        users = User.query.all()
        self.assertEqual(len(users), 2)

        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = u1.id

            resp = c.post(f"/users/follow/{u2.id}")

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(u1.following[0].id, u2.id)