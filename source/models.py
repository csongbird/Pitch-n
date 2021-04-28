from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """
    This is the user class used for individuals
    """
    __tablename__ = "Individual Users"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, username, password, email, **kwargs):
        self.username = username
        self.password = password
        self.email = email
        self.favorites = []

    def get_user_with_id(user_id):
        return User.query.filter_by(user_id=user_id).first()

    def add_favorite(self, org_id):
        if(org_id in self.favorites):
            return
        self.favorites.append(org_id)

    def remove_favorite(self, org_id):
        if(org_id in self.favorites):
            self.favorites.remove(org_id)
        return

    def json(self):
        return {'username': self.username, 'email': self.email}

    def __repr__(self):
        return '<User %r>' % self.username


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

    def __init__(self, name, password, location, **kwargs):
        self.name = name
        self.password = password
        self.location = location

    def get_org_with_id(org_id):
        return Organization.query.filter_by(org_id=org_id).first()

    def json(self):
        return {'name': self.name,
                'email': self.email,
                'location': self.location}

    def __repr__(self):
        return '<Organizatoin %r>' % self.name
