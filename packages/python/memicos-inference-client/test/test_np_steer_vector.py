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

from memicos_inference_client.models.np_steer_vector import NPSteerVector

class TestNPSteerVector(unittest.TestCase):
    """NPSteerVector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NPSteerVector:
        """Test NPSteerVector
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NPSteerVector`
        """
        model = NPSteerVector()
        if include_optional:
            return NPSteerVector(
                steering_vector = [
                    1.337
                    ],
                strength = 1.337,
                hook = 'blocks.0.hook_resid_pre'
            )
        else:
            return NPSteerVector(
                steering_vector = [
                    1.337
                    ],
                strength = 1.337,
                hook = 'blocks.0.hook_resid_pre',
        )
        """

    def testNPSteerVector(self):
        """Test NPSteerVector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
