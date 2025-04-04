# coding: utf-8

"""
    Wise Platform API

    Comprehensive API for Wise platform services including: - Profile - Activity tracking and management - Quote creation and management - Recipient - Transfer 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wise_api_client.models.transfer_requirements_response_inner import TransferRequirementsResponseInner

class TestTransferRequirementsResponseInner(unittest.TestCase):
    """TransferRequirementsResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransferRequirementsResponseInner:
        """Test TransferRequirementsResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransferRequirementsResponseInner`
        """
        model = TransferRequirementsResponseInner()
        if include_optional:
            return TransferRequirementsResponseInner(
                type = 'transfer',
                fields = [
                    wise_api_client.models.transfer_requirements_response_inner_fields_inner.TransferRequirementsResponse_inner_fields_inner(
                        name = '', 
                        group = [
                            wise_api_client.models.requirement_field.RequirementField(
                                key = '', 
                                name = '', 
                                type = 'text', 
                                refresh_requirements_on_change = True, 
                                required = True, 
                                display_format = '', 
                                example = '', 
                                min_length = 56, 
                                max_length = 56, 
                                validation_regexp = '', 
                                values_allowed = [
                                    wise_api_client.models.account_requirements_inner_fields_inner_group_inner_values_allowed_inner.AccountRequirements_inner_fields_inner_group_inner_valuesAllowed_inner(
                                        key = '', 
                                        name = '', )
                                    ], )
                            ], )
                    ]
            )
        else:
            return TransferRequirementsResponseInner(
        )
        """

    def testTransferRequirementsResponseInner(self):
        """Test TransferRequirementsResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
