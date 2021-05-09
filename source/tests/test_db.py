from unittest import TestCase
import source.db as db
from source.models import User
from source.__init__ import create_app

create_app().app_context().push()


class DBTestCase(TestCase):
    def test_fetch_locations(self):
        locations = db.fetch_locations()
        self.assertTrue(isinstance(locations, dict))
        self.assertTrue(len(locations) > 1)


    def test_add_user(self):
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

    def test_edit_user(self):
        info = db.set_user_info()
        self.assertIn("updated", info)


    """def test_add_org(self):
        db.add_org("Test Charity", "password", "charity@yahoo.com", "address")
        org = Organization.query.filter(location="address").first()
        assert(org != None)"""

    
    def test_edit_org(self):
        info = db.set_org_info()
        self.assertIn("updated", info)


    """ def test_remove_org(self):
        org = remove_org(1)
        self.assertIn("removed", org) """