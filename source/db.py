"""
This file will manage interactions with the database.
"""
from models import db, User, Organization


def fetch_locations():
    """
    A function to return all locations
    """
    return {"Bob's Burgers": 2, "Joe's Soup Kitchen": 1, "Cat Shelter": 2}


def add_user():
    """
    A function to add the user to the database
    """
    return "user added"


def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return User.json()
    return {'message':'user not found'},404


def set_user_info():
    """
    A function to edit user's profile information
    """
    return "profile updated"


def remove_user(user_id):
    """
    A function to remove the user from the database
    """
    user = User.get_user_with_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message':'user deleted'}
    else:
        return {'message':'user not found'},404


def add_org():
    """
    A function to add the organization to the database
    """
    return "organization added"


def get_org(name):
    org = Organization.query.filter_by(name=name).first()
    if org:
        return org.json()
    return {'message':'organization not found'},404


def set_org_info():
    """
    A function to edit the organzation's information
    """
    return "profile updated"


def remove_org(org_id):
    """
    A function to remove the organization from the database
    """
    org = Organization.get_org_with_id(org_id)
    if org:
        db.session.delete(org)
        db.session.commit()
        return {'message':'organization removed'}
    else:
        return {'message':'organization not found'},404
