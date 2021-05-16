"""
This file will manage interactions with the database.
"""
from source.models import db, User, Organization
from werkzeug.security import generate_password_hash


def fetch_locations():
    """
    Returns all locations
    """
    return {"Bob's Burgers": 2, "Joe's Soup Kitchen": 1, "Cat Shelter": 2}


def add_user(email, username, password):
    """
    Adds a user to the database
    """
    new_user = User.get_user(email, username, password)
    if new_user[1] == 200:
        return "user exists"
    new_user = User(
        email=email,
        username=username,
        password=generate_password_hash(password, method='sha256')
    )
    db.session.add(new_user)
    db.session.commit()
    return "user added"


def get_user_with_id(user_id):
    """
    Returns a user
    """
    user = User.get_user_with_id(user_id)
    if user:
        return user.json(), 200
    return {'message': 'user not found'}, 404


def get_user(email, username, password):
    """
    Returns a user given their email, username, and password
    """
    user = User.get_user(email, username, password)
    if user[1] != 200:
        return {'message': 'user not found'}, 404
    return user[0].json(), 200


def set_user_info():
    """
    Edit a user's profile information
    """
    return "profile updated"


def remove_user(user_id):
    """
    Remove a user from the database
    """
    user = User.get_user_with_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': 'user deleted'}, 200
    else:
        return {'message': 'user not found'}, 404


def add_org(email, username, password, name, location):
    """
    Add an organization to the database
    """
    new_org = Organization.get_org(email, username, password, name, location)
    if new_org[1] == 200:
        return "organization exists"
    new_org = Organization(name, username, password, location, email)
    db.session.add(new_org)
    db.session.commit()
    return "organization added"


def get_org(email, username, password, name, location):
    """
    Returns a organization gien their email, username, password
    name, and location
    """
    org = Organization.get_org(email, username, password, name, location)
    if org[1] != 200:
        return {'message': 'organization not found'}, 404
    return org[0].json(), 200


def set_org_info():
    """
    Edit an organzation's information
    """
    return "profile updated"


def remove_org(org_id):
    """
    Remove an organization from the database
    """
    org = Organization.get_org_with_id(org_id)
    if org:
        db.session.delete(org)
        db.session.commit()
        return {'message': 'organization removed'}
    else:
        return {'message': 'organization not found'}, 404
