# coding: utf-8

"""
    Wise Platform API

    Comprehensive API for Wise platform services including: - Profile - Activity tracking and management - Quote creation and management - Recipient - Transfer 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wise_api_client.models.create_personal_profile_request import CreatePersonalProfileRequest

class TestCreatePersonalProfileRequest(unittest.TestCase):
    """CreatePersonalProfileRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePersonalProfileRequest:
        """Test CreatePersonalProfileRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePersonalProfileRequest`
        """
        model = CreatePersonalProfileRequest()
        if include_optional:
            return CreatePersonalProfileRequest(
                first_name = '',
                last_name = '',
                address = wise_api_client.models.create_personal_profile_request_address.createPersonalProfile_request_address(
                    address_first_line = '', 
                    city = '', 
                    country_iso3_code = '', ),
                contact_details = wise_api_client.models.create_personal_profile_request_contact_details.createPersonalProfile_request_contactDetails(
                    email = '', 
                    phone_number = '', )
            )
        else:
            return CreatePersonalProfileRequest(
                first_name = '',
                last_name = '',
                address = wise_api_client.models.create_personal_profile_request_address.createPersonalProfile_request_address(
                    address_first_line = '', 
                    city = '', 
                    country_iso3_code = '', ),
                contact_details = wise_api_client.models.create_personal_profile_request_contact_details.createPersonalProfile_request_contactDetails(
                    email = '', 
                    phone_number = '', ),
        )
        """

    def testCreatePersonalProfileRequest(self):
        """Test CreatePersonalProfileRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
