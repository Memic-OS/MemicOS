# coding: utf-8

"""
    MemicOS - Inference Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1.0
    Contact: johnny@memicos.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from memicos_inference_client.models.activation_single_post200_response import ActivationSinglePost200Response

class TestActivationSinglePost200Response(unittest.TestCase):
    """ActivationSinglePost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivationSinglePost200Response:
        """Test ActivationSinglePost200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivationSinglePost200Response`
        """
        model = ActivationSinglePost200Response()
        if include_optional:
            return ActivationSinglePost200Response(
                activation = memicos_inference_client.models._activation_single_post_200_response_activation._activation_single_post_200_response_activation(
                    values = [
                        1.337
                        ], 
                    max_value = 1.337, 
                    max_value_index = 56, 
                    dfa_values = [
                        1.337
                        ], 
                    dfa_max_value = 1.337, 
                    dfa_target_index = 56, ),
                tokens = [
                    ''
                    ]
            )
        else:
            return ActivationSinglePost200Response(
                activation = memicos_inference_client.models._activation_single_post_200_response_activation._activation_single_post_200_response_activation(
                    values = [
                        1.337
                        ], 
                    max_value = 1.337, 
                    max_value_index = 56, 
                    dfa_values = [
                        1.337
                        ], 
                    dfa_max_value = 1.337, 
                    dfa_target_index = 56, ),
                tokens = [
                    ''
                    ],
        )
        """

    def testActivationSinglePost200Response(self):
        """Test ActivationSinglePost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
