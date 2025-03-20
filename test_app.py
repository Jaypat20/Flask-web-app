import unittest
from app import create_app, db
from app.models import User
import json

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Create app with test configuration
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()
            # Add a sample user for testing
            user = User(name="Alice", email="alice@example.com")
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Simple Text Page", response.data)
        
    def test_users_page(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Alice", response.data)
        self.assertIn(b"alice@example.com", response.data)
        
    def test_add_user(self):
        # Test adding a new user via POST endpoint
        new_user = {"name": "Bob", "email": "bob@example.com"}
        response = self.client.post('/user', json=new_user)
        self.assertEqual(response.status_code, 201)
        with self.app.app_context():
            user = User.query.filter_by(name="Bob").first()
            self.assertIsNotNone(user)
            self.assertEqual(user.email, "bob@example.com")
        
if __name__ == '__main__':
    unittest.main()
