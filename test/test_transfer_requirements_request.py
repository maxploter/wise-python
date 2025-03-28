# coding: utf-8

"""
    Wise Platform API

    Comprehensive API for Wise platform services including: - Profile - Activity tracking and management - Quote creation and management - Recipient - Transfer 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wise_api_client.models.transfer_requirements_request import TransferRequirementsRequest

class TestTransferRequirementsRequest(unittest.TestCase):
    """TransferRequirementsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransferRequirementsRequest:
        """Test TransferRequirementsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransferRequirementsRequest`
        """
        model = TransferRequirementsRequest()
        if include_optional:
            return TransferRequirementsRequest(
                target_account = 56,
                quote_uuid = '',
                details = None,
                customer_transaction_id = ''
            )
        else:
            return TransferRequirementsRequest(
                target_account = 56,
                quote_uuid = '',
        )
        """

    def testTransferRequirementsRequest(self):
        """Test TransferRequirementsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
