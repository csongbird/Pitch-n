"""
This is the file containing all the endpoints for our flask app.
The endpoint called 'endpoints' will return all available endpoints.
"""

from flask import request
from flask_api import FlaskAPI
from flask_restx import Resource, Api, fields
from source.db import fetch_locations

app = FlaskAPI(__name__)
api = Api(app)

AVAILABLE = 'Available endpoints:'


user = api.model('User', {
    'username': fields.String(required=True)
})


list_of_users = {}


@api.route("/user/<int:id>")
class Users(Resource):
    def get(self, id):
        id = list_of_users[id]
        return {"name": list_of_users[id]}

    @api.expect(user)
    def post(self, id):
        list_of_users[id] = request.json['name']
        return {"name": list_of_users[id]}


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
        return {AVAILABLE: endpoints}


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
