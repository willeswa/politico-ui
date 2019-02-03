""" Defines political office models """

# Standard imports
import datetime

# Third party imports
from flask import make_response, jsonify

DB = [
    {
        "created_on": "Sunday, 03. February 2019 06:52PM",
        "name": "President of the Republic of Kenya",
        "office_id": 1,
        "office_type": "Valid Office Type"
    }
]


class OfficeModel:
    """ Handles operations related to politicsl offices """

    def __init__(self, office_type, name):
        """ Defines instance variables """

        self.office_type = office_type
        self.name = name
        self.office_id = len(DB) + 1
        self.created_on = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

    def create_office(self):
        """ creates a political office """

        try:
            office = {}
            office['name'] = self.name
            office['office_type'] = self.office_type
            office['office_id'] = self.office_id
            office['created_on'] = self.created_on

            DB.append(office)
            response = make_response(
                jsonify({'status': 201, 'message': 'Successfuly created office'}), 201)
            return response

        except Exception as error:
            raise Exception({'error': error})

    @classmethod
    def retrieve_all_offices(cls):
        """ Retrieves all offices from the database """
        response = make_response(
            jsonify({'status': 200, 'message': DB}), 200
        )
        return response

    @classmethod
    def get_specific_office(cls, office_id):
        """ returns a specific office given office id """

        if OfficeModel.office_exists(office_id):
            response = make_response(
                jsonify({'status': 200, 'message': OfficeModel.office_exists(office_id)}), 200)
            return response
        return make_response(jsonify({'status': 404, 'message': 'Office not found'}), 404)

    @classmethod
    def office_exists(cls, office_id):
        """ Checks if a specific office exists """

        for office in DB:
            if office['office_id'] == office_id:
                return office
        return None