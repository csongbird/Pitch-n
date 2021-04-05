"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data
Gradually, we will fill in actuall calls to our datastore.
"""


def fetch_locations():
    """
    A function to return all locations
    """
    return {"Bob's Burgers": 2, "Joe's Soup Kitchen": 1, "Cat Shelter": 2}


def add_user():
    """
    A function to add the user to the database
    """
    return {"user added"}


def set_user_info():
    """
    A function to edit user's profile information
    """
    return {"profile updated"}


def remove_user():
    """
    A function to remove the user from the database
    """
    return {"user deleted"}


def add_org():
    """
    A function to add the organization to the database
    """
    return {"organization added"}


def set_org_info():
    """
    A function to edit the organzation's information
    """
    return {"profile updated"}


def remove_org():
    """
    A function to remove the organization from the database
    """
    return {"organization removed"}
