from unittest import TestCase

from source.db import (
    fetch_locations,
    add_user,
    set_user_info,
    remove_user,
    add_org,
    set_org_info,
    remove_org,
)


class DBTestCase(TestCase):
    def test_fetch_locations(self):
        locations = fetch_locations()
        self.assertTrue(isinstance(locations, dict))
        self.assertTrue(len(locations) > 1)


    def test_add_user(self):
        user = add_user();
        self.assertIn("user", user);


    def test_edit_user(self):
        info = set_user_info();
        self.assertIn("updated", info);


    def test_remove_user(self):
        user = remove_user();
        self.assertIn("deleted", user);


    def test_add_org(self):
        org = add_org();
        self.assertIn("organization", org);

    
    def test_edit_org(self):
        info = set_org_info();
        self.assertIn("updated", info);


    def test_remove_org(self):
        org = remove_org();
        self.assertIn("removed", org);