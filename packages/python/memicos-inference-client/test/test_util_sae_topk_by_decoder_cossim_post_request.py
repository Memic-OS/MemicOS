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

from memicos_inference_client.models.util_sae_topk_by_decoder_cossim_post_request import UtilSaeTopkByDecoderCossimPostRequest

class TestUtilSaeTopkByDecoderCossimPostRequest(unittest.TestCase):
    """UtilSaeTopkByDecoderCossimPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UtilSaeTopkByDecoderCossimPostRequest:
        """Test UtilSaeTopkByDecoderCossimPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UtilSaeTopkByDecoderCossimPostRequest`
        """
        model = UtilSaeTopkByDecoderCossimPostRequest()
        if include_optional:
            return UtilSaeTopkByDecoderCossimPostRequest(
                feature = memicos_inference_client.models.np_feature.NPFeature(
                    model = 'gpt2-small', 
                    source = '0-res-jb', 
                    index = 14057, ),
                vector = [
                    1.337
                    ],
                model = '',
                source = '',
                num_results = 56
            )
        else:
            return UtilSaeTopkByDecoderCossimPostRequest(
                model = '',
                source = '',
                num_results = 56,
        )
        """

    def testUtilSaeTopkByDecoderCossimPostRequest(self):
        """Test UtilSaeTopkByDecoderCossimPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
