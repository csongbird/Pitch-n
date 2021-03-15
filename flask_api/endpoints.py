"""
This is the file containing all the endpoints for our flask app.
The endpoint called 'endpoints' will return all available endpoints.
"""

from flask_api import FlaskAPI
from flask_restx import Resource, Api
from db import fetch_locations

app = FlaskAPI(__name__)
api = Api(app)


@api.route('/')
class Home(Resource):
    """
    The purpose of the Home class is to test if
    the app is working.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        Returns "success"
        """
        return {'success'}


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class serves as a live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        the get() method will return a list of available endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


@api.route('/locations')
class Locations(Resource):
    """
    This class supports fetching a list of locations
    """
    def get(self):
        """
        This method returns all locations.
        """
        return fetch_locations()


if __name__ == "__main__":
    app.run()
