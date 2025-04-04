# coding: utf-8

"""
    Wise Platform API

    Comprehensive API for Wise platform services including: - Profile - Activity tracking and management - Quote creation and management - Recipient - Transfer 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wise_api_client.models.create_recipient_request import CreateRecipientRequest

class TestCreateRecipientRequest(unittest.TestCase):
    """CreateRecipientRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateRecipientRequest:
        """Test CreateRecipientRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateRecipientRequest`
        """
        model = CreateRecipientRequest()
        if include_optional:
            return CreateRecipientRequest(
                currency = 'GBP',
                type = 'sort_code',
                profile = 30000000,
                account_holder_name = 'John Doe',
                owned_by_customer = True,
                details = wise_api_client.models.create_recipient_request_details.CreateRecipientRequest_details(
                    legal_type = 'PRIVATE', 
                    sort_code = '', 
                    account_number = '', 
                    date_of_birth = 'Sun Jan 01 00:00:00 UTC 1961', )
            )
        else:
            return CreateRecipientRequest(
                currency = 'GBP',
                type = 'sort_code',
                profile = 30000000,
                account_holder_name = 'John Doe',
                details = wise_api_client.models.create_recipient_request_details.CreateRecipientRequest_details(
                    legal_type = 'PRIVATE', 
                    sort_code = '', 
                    account_number = '', 
                    date_of_birth = 'Sun Jan 01 00:00:00 UTC 1961', ),
        )
        """

    def testCreateRecipientRequest(self):
        """Test CreateRecipientRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
