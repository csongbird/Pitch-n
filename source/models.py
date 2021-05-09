from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """
    This is the user class used for individuals
    """
    # __tablename__ = "Individual Users"
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def get_id(self):
        return self.user_id

    def get_user_with_id(user_id):
        return User.query.filter_by(user_id=user_id).first()


class Organization(db.Model):
    """
    This is the class used for organizations
    """
    __tablename__ = "Organizations"

    org_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    location = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, name, password, location, email):
        self.name = name
        self.password = password
        self.location = location
        self.email = email

    def get_org_with_id(org_id):
        return Organization.query.filter_by(org_id=org_id).first()

    def get_id(self):
        return self.org_id

    def json(self):
        return {'name': self.name,
                'email': self.email,
                'location': self.location}

    def __repr__(self):
        return '<Organizatoin %r>' % self.name
