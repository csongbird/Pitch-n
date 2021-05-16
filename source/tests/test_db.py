from unittest import TestCase
from warnings import resetwarnings
import source.db as db
from source.models import Organization, User
from source.__init__ import create_app

create_app().app_context().push()


class DBTestCase(TestCase):
    def test_add_remove_user(self):
        """
        Test for adding and removing a user
        """
        exists = User.query.filter_by(email="email@nyu.edu").first()
        print(exists)
        if exists:
            db.remove_user(exists.get_id())
        status = db.add_user("email@nyu.edu", "usertest", "12345")
        user = User.query.filter_by(username="usertest").first()
        assert(user != None)
        if user:
            user_id = user.get_id()
            a = db.remove_user(user_id)
            user = User.query.filter_by(username="usertest").first()
        assert(user == None)

        db.add_user("email@nyu.edu", "usertest", "12345")
        user = User.query.filter_by(email="email@nyu.edu").first()
        assert (user != None)

        if user:
            user_id = user.get_id()
            a = db.remove_user(user_id)
            user = User.query.filter_by(username="usertest").first()
        assert(user == None)

    def test_get_user(self):
        """
        Test for getting a user
        """
        exists = User.query.filter_by(email="email@nyu.edu").first()
        if exists:
            db.remove_user(exists.get_id())
        db.add_user("email@nyu.edu", "usertest", "12345")
        user = User.query.filter_by(username="usertest").first()
        assert (user != None)
        response = db.get_user("email@nyu.edu", "usertest", "12345")
        assert (response[1] == 200)
        user_id = user.get_id()
        a = db.remove_user(user_id)
        user = User.query.filter_by(username="usertest").first()
        assert(user == None)

    def test_get_org(self):
        """
        Test for getting a user
        """
        exists = Organization.query.filter_by(email="orgtest@nyu.edu").first()
        if exists:
            db.remove_org(exists.get_id())
        db.add_org("orgtest@nyu.edu", "orgtest", "12345", "test", "test")
        org = Organization.query.filter_by(username="orgtest").first()
        assert (org != None)
        response = db.get_org("orgtest@nyu.edu", "orgtest", "12345", "test", "test")
        assert (response[1] == 200)
        org_id = org.get_id()
        a = db.remove_org(org_id)
        org = Organization.query.filter_by(username="orgtest").first()
        assert(org == None)

    """def test_add_remove_org(self):
        db.add_org("Test Charity", "password", "charity@yahoo.com", "address")
        org = Organization.query.filter(location="address").first()
        assert(org != None)"""

    def test_get_user_with_id(self):
        """
        Test to see if we can get a user with their id
        """
        exists = User.query.filter_by(email="email@nyu.edu").first()
        if exists:
            db.remove_user(exists.get_id())
        status = db.add_user("email@nyu.edu", "usertest", "12345")
        user = User.query.filter_by(username="usertest").first()
        assert (user != None)
        response = db.get_user_with_id(user.get_id())
        assert (response[1] == 200)
    
    def test_remove_user_with_user_id(self):
        """
        Test to see if we can remove a user with their id
        """
        exists = User.query.filter_by(email="email@nyu.edu").first()
        if exists:
            db.remove_user(exists.get_id())
        status = db.add_user("email@nyu.edu", "usertest", "12345")
        user = User.query.filter_by(username="usertest").first()
        assert (user != None)
        response = db.remove_user(user.get_id())
        assert (response[0] != 404)
    

    def test_get_user(self):
        exists = User.query.filter_by(email="email@nyu.edu").first()
        if exists:
            db.remove_user(exists.get_id())
        status = db.add_user("email@nyu.edu", "usertest", "12345")
        user = db.get_user("email@nyu.edu", "usertest", "12345")
        assert (user[1] != 404)
        db.remove_user(user[0]["user_id"])
        user = User.query.filter_by(username="usertest").first()
        assert(user == None)