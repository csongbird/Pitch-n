from unittest import TestCase
from flask import url_for, request
from source.__init__ import create_app

class TestApp(TestCase):
    def setUp(self):
        """
        Test for setup
        """
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()


    def test_home_page(self):
        """
        Test to see if we can access the homepage
        """
        res = self.client.get('/')
        self.assertTrue('<html>' in res.get_data(as_text=True))


    def test_user_login(self):
        """
        Test to see if a user can login
        """
        with self.app.test_client() as client:
            testUser = {'uname': 'test', 'psw': 'test', 'remember': 'True'}
            res = client.post('/login', data=testUser, follow_redirects=True)
            assert(request.path == url_for('main.profile'))


    def test_org_login(self):
        """
        Test to see if an org can login
        """
        with self.app.test_client() as client:
            testOrg = {'uname': 'org1', 'psw': 'org1'}
            res = client.post('/login', data=testOrg, follow_redirects=True)
            assert(request.path == url_for('main.organization'))


    def test_register_page(self):
        """
        Test to see if we can get the registion page
        """
        res = self.client.get('/signup')
        self.assertTrue('<html>' in res.get_data(as_text=True))


    def test_user_registration(self):
        """
        Test to see if a user can register
        """
        with self.app.test_client() as client:
            testUser = {'email': 'email@nyu.edu', 
                'uname': 'usertest', 
                'psw': '12345'}
            res = client.post('/signup', data=testUser, follow_redirects=True)
            assert(request.path == url_for('login'))


    def test_org_registration(self):
        """
        Test to see if an organization can register
        """
        with self.app.test_client() as client:
            testUser = {'email': 'email@nyu.edu', 
                'uname': 'usertest', 
                'psw': '12345',
                'yes': 'True',
                'name': 'testCharity',
                'loc': 'testAddress'}
            res = client.post('/signup', data=testUser, follow_redirects=True)
            assert(request.path == url_for('signup'))


    def test_logout_page(self):
        """
        Test to see if loging out works
        """
        with self.app.test_client() as client:
            res = client.get('/logout', follow_redirects=True)
            assert(request.path == url_for('login'))