# coding: utf-8

"""
    Wise Platform API

    Comprehensive API for Wise platform services including: - Profile - Activity tracking and management - Quote creation and management - Recipient - Transfer 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wise_api_client.models.recipient_details import RecipientDetails

class TestRecipientDetails(unittest.TestCase):
    """RecipientDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecipientDetails:
        """Test RecipientDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecipientDetails`
        """
        model = RecipientDetails()
        if include_optional:
            return RecipientDetails(
                reference = '',
                sort_code = '040075',
                account_number = '37778842'
            )
        else:
            return RecipientDetails(
        )
        """

    def testRecipientDetails(self):
        """Test RecipientDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
