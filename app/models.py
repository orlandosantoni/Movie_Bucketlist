from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(UserMixin, db.Model):
    """
    Create a User table
    """

    # Ensures table will be named in plural and not in singular
    # As is the name of the model

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    movies = db.relationship('Movie', backref='User', lazy='dynamic')
    
    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('Password is not a readable entity')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matched actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User: {}'.format(self.username)


class Movie(db.Model):
    """
    Create a Movie table
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(80))
    director = db.Column(db.String(60))
    imdb_rating = db.Column(db.Float)
    metacritic_rating = db.Column(db.Integer)
    user_rating = db.Column(db.Float)

    def __repr__(self):
        return '<Movie: {}>'.format(self.title)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

