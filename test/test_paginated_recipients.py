# coding: utf-8

"""
    Wise Platform API

    Comprehensive API for Wise platform services including: - Profile - Activity tracking and management - Quote creation and management - Recipient - Transfer 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wise_api_client.models.paginated_recipients import PaginatedRecipients

class TestPaginatedRecipients(unittest.TestCase):
    """PaginatedRecipients unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedRecipients:
        """Test PaginatedRecipients
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedRecipients`
        """
        model = PaginatedRecipients()
        if include_optional:
            return PaginatedRecipients(
                content = [
                    wise_api_client.models.recipient.Recipient(
                        id = 40000000, 
                        creator_id = 41000000, 
                        profile_id = 30000000, 
                        name = wise_api_client.models.recipient_name.Recipient_name(
                            full_name = 'John Doe', 
                            given_name = '', 
                            family_name = '', 
                            middle_name = '', ), 
                        currency = 'GBP', 
                        country = 'GB', 
                        type = 'SortCode', 
                        legal_entity_type = 'PERSON', 
                        active = True, 
                        details = wise_api_client.models.recipient_details.Recipient_details(
                            reference = '', 
                            sort_code = '040075', 
                            account_number = '37778842', ), 
                        common_field_map = wise_api_client.models.recipient_common_field_map.Recipient_commonFieldMap(
                            bank_code_field = 'sortCode', ), 
                        hash = '', 
                        account_summary = '', 
                        long_account_summary = '', 
                        display_fields = [
                            wise_api_client.models.recipient_display_fields_inner.Recipient_displayFields_inner(
                                key = '', 
                                label = '', 
                                value = '', )
                            ], 
                        owned_by_customer = True, )
                    ],
                size = 1
            )
        else:
            return PaginatedRecipients(
        )
        """

    def testPaginatedRecipients(self):
        """Test PaginatedRecipients"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
