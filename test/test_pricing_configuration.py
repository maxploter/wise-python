# coding: utf-8

"""
    Wise Platform API

    Comprehensive API for Wise platform services including: - Profile - Activity tracking and management - Quote creation and management - Recipient - Transfer 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wise_api_client.models.pricing_configuration import PricingConfiguration

class TestPricingConfiguration(unittest.TestCase):
    """PricingConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PricingConfiguration:
        """Test PricingConfiguration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PricingConfiguration`
        """
        model = PricingConfiguration()
        if include_optional:
            return PricingConfiguration(
                fee = wise_api_client.models.fee_configuration.FeeConfiguration(
                    type = 'OVERRIDE', 
                    variable = 1.337, 
                    fixed = 1.337, )
            )
        else:
            return PricingConfiguration(
        )
        """

    def testPricingConfiguration(self):
        """Test PricingConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
