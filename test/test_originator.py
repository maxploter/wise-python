# coding: utf-8

"""
    Wise Platform API

    Comprehensive API for Wise platform services including: - Profile - Activity tracking and management - Quote creation and management - Recipient - Transfer 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wise_api_client.models.originator import Originator

class TestOriginator(unittest.TestCase):
    """Originator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Originator:
        """Test Originator
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Originator`
        """
        model = Originator()
        if include_optional:
            return Originator(
                legal_entity_type = 'PRIVATE',
                reference = '',
                name = wise_api_client.models.originator_name.OriginatorName(
                    given_name = '', 
                    middle_names = [
                        ''
                        ], 
                    family_name = '', 
                    patronymic_name = '', 
                    full_name = '', ),
                date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                business_registration_code = '',
                address = wise_api_client.models.originator_address.OriginatorAddress(
                    first_line = '', 
                    city = '', 
                    state_code = '', 
                    country_code = 'AE', 
                    post_code = '', ),
                account_details = ''
            )
        else:
            return Originator(
                legal_entity_type = 'PRIVATE',
                reference = '',
                address = wise_api_client.models.originator_address.OriginatorAddress(
                    first_line = '', 
                    city = '', 
                    state_code = '', 
                    country_code = 'AE', 
                    post_code = '', ),
        )
        """

    def testOriginator(self):
        """Test Originator"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
