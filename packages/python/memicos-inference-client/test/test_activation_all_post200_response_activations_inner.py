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

from memicos_inference_client.models.activation_all_post200_response_activations_inner import ActivationAllPost200ResponseActivationsInner

class TestActivationAllPost200ResponseActivationsInner(unittest.TestCase):
    """ActivationAllPost200ResponseActivationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivationAllPost200ResponseActivationsInner:
        """Test ActivationAllPost200ResponseActivationsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivationAllPost200ResponseActivationsInner`
        """
        model = ActivationAllPost200ResponseActivationsInner()
        if include_optional:
            return ActivationAllPost200ResponseActivationsInner(
                source = '',
                index = 56,
                values = [
                    1.337
                    ],
                sum_values = 1.337,
                max_value = 1.337,
                max_value_index = 1.337,
                dfa_values = [
                    1.337
                    ],
                dfa_target_index = 56,
                dfa_max_value = 1.337
            )
        else:
            return ActivationAllPost200ResponseActivationsInner(
                source = '',
                index = 56,
                values = [
                    1.337
                    ],
                max_value = 1.337,
                max_value_index = 1.337,
        )
        """

    def testActivationAllPost200ResponseActivationsInner(self):
        """Test ActivationAllPost200ResponseActivationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
