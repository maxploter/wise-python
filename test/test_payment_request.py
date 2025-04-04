# coding: utf-8

"""
    Wise Platform API

    Comprehensive API for Wise platform services including: - Profile - Activity tracking and management - Quote creation and management - Recipient - Transfer 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wise_api_client.models.payment_request import PaymentRequest

class TestPaymentRequest(unittest.TestCase):
    """PaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentRequest:
        """Test PaymentRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentRequest`
        """
        model = PaymentRequest()
        if include_optional:
            return PaymentRequest(
                type = 'BALANCE',
                partner_reference = ''
            )
        else:
            return PaymentRequest(
                type = 'BALANCE',
        )
        """

    def testPaymentRequest(self):
        """Test PaymentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
