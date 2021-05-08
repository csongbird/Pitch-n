"""
This file will manage interactions with the database.
"""
from source.models import db, User, Organization


def fetch_locations():
    """
    Returns all locations
    """
    return {"Bob's Burgers": 2, "Joe's Soup Kitchen": 1, "Cat Shelter": 2}


def add_user(email, username, password):
    """
    Adds a user to the database
    """
    new_user = User(
        email=email,
        username=username,
        password=password
    )
    db.session.add(new_user)
    db.session.commit()
    return "user added"


def get_user(user_id):
    """
    Returns a user
    """
    user = User.get_user_with_id(user_id)
    if user:
        return User.json()
    return {'message': 'user not found'}, 404


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
        return {'message': 'user deleted'}
    else:
        return {'message': 'user not found'}, 404


def add_org(name, password, email, location):
    """
    Add an organization to the database
    """
    new_org = Organization(
        name=name,
        password=password,
        email=email,
        location=location
    )
    db.session.add(new_org)
    db.session.commit()
    return "organization added"


def get_org(name):
    org = Organization.query.filter_by(name=name).first()
    if org:
        return org.json()
    return {'message': 'organization not found'}, 404


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
