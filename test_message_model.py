import os
from unittest import TestCase
from models import db, User, Message, Follows

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"
from app import app

app.config['WTF_CSRF_ENABLED'] = False

class MessageModelTestCase(TestCase):
    def setUp(self):
        """Create test client, add sample data."""
        db.drop_all()
        db.create_all()
        self.client = app.test_client()
        self.testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="testuser",
                                    image_url=None)
        db.session.commit()

    def test_message_model(self):
        """Create user first for foreign key constraint"""
        m = Message(
            text="First message!",
            user_id=1
        )
        db.session.add(m)
        db.session.commit()

        # Message should be assigned to user_id 1
        msg = Message.query.one()
        self.assertEqual(msg.user_id, 1)