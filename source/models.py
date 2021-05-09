from .__init__ import database as db
from flask_login import UserMixin, login_user
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """
    This is the user class used for individuals
    """
    # __tablename__ = "Individual Users"
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def json(self):
        return {'user_id': self.user_id,
                'email': self.email,
                'username': self.username}

    def get_id(self):
        """
        Returns the user_id of the User
        """
        return self.user_id

    def get_user_with_id(user_id):
        """
        Returns the User from the database using the user_id
        """
        return User.query.filter_by(user_id=user_id).first()

    def get_user(email, username, password):
        """
        From the database returns the user and a code 200,
        else returns a user not found and error code 404
        """
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return {'message': 'user not found'}, 404
        return user, 200

    def login(email, username, password, remember):
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return {'message': 'user not found'}, 404
        login_user(user, remember=remember)
        return {'message': 'logged in'}, 200


class Organization(UserMixin, db.Model):
    """
    This is the class used for organizations
    """
    __tablename__ = "Organizations"

    org_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    location = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, name, username, password, location, email):
        self.name = name
        self.username = username
        self.password = generate_password_hash(password, method='sha256')
        self.location = location
        self.email = email

    def get_org_with_id(org_id):
        return Organization.query.filter_by(org_id=org_id).first()

    def get_org(email, username, password, name, location):
        """
        From the database returns the organization and a code 200,
        else returns an organizaiton not found and error code 404
        """
        org = Organization.query.filter_by(email=email).first()
        if not org:
            org = Organization.query.filter_by(username=username).first()
        if not org:
            org = Organization.query.filter_by(name=name).first()
        if not org:
            org = Organization.query.filter_by(location=location).first()
        if not org or not check_password_hash(org.password, password):
            return {'message': 'organization not found'}, 404
        return org, 200

    def get_id(self):
        return self.org_id

    def json(self):
        return {'org_id': self.org_id,
                'name': self.name,
                'email': self.email,
                'username': self.username,
                'location': self.location}

    def login(email, username, password, remember):
        org = Organization.query.filter_by(email=email).first()
        if not org:
            org = Organization.query.filter_by(username=username).first()
        if not org or not check_password_hash(org.password, password):
            return {'message': 'organization not found'}, 404
        login_user(org, remember=remember)
        return {'message': 'logged in'}, 200

    def __repr__(self):
        return '<Organization %r>' % self.name
