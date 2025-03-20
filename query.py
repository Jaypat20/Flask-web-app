from app import create_app, db
from app.models import User

def add_user(name, email):
    app = create_app()
    with app.app_context():
        todo = User.query.filter_by(name=name).first()
        if todo:
            print("User already Present.")
            return
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        print(f"User {name} added successfully.")

if __name__ == '__main__':
    # Example usage: add a test user.
    add_user("John Doe", "john@example.com")
    add_user("John Dow", "john1@example.com")
