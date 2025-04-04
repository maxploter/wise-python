# coding: utf-8

"""
    Wise Platform API

    Comprehensive API for Wise platform services including: - Profile - Activity tracking and management - Quote creation and management - Recipient - Transfer 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wise_api_client.models.v1_profiles_profile_id_verification_documents_post_request import V1ProfilesProfileIdVerificationDocumentsPostRequest

class TestV1ProfilesProfileIdVerificationDocumentsPostRequest(unittest.TestCase):
    """V1ProfilesProfileIdVerificationDocumentsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ProfilesProfileIdVerificationDocumentsPostRequest:
        """Test V1ProfilesProfileIdVerificationDocumentsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ProfilesProfileIdVerificationDocumentsPostRequest`
        """
        model = V1ProfilesProfileIdVerificationDocumentsPostRequest()
        if include_optional:
            return V1ProfilesProfileIdVerificationDocumentsPostRequest(
                type = 'DRIVERS_LICENCE',
                unique_identifier = ''
            )
        else:
            return V1ProfilesProfileIdVerificationDocumentsPostRequest(
                type = 'DRIVERS_LICENCE',
                unique_identifier = '',
        )
        """

    def testV1ProfilesProfileIdVerificationDocumentsPostRequest(self):
        """Test V1ProfilesProfileIdVerificationDocumentsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
