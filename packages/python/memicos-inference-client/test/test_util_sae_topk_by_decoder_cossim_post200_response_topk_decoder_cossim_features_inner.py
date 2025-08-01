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

from memicos_inference_client.models.util_sae_topk_by_decoder_cossim_post200_response_topk_decoder_cossim_features_inner import UtilSaeTopkByDecoderCossimPost200ResponseTopkDecoderCossimFeaturesInner

class TestUtilSaeTopkByDecoderCossimPost200ResponseTopkDecoderCossimFeaturesInner(unittest.TestCase):
    """UtilSaeTopkByDecoderCossimPost200ResponseTopkDecoderCossimFeaturesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UtilSaeTopkByDecoderCossimPost200ResponseTopkDecoderCossimFeaturesInner:
        """Test UtilSaeTopkByDecoderCossimPost200ResponseTopkDecoderCossimFeaturesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UtilSaeTopkByDecoderCossimPost200ResponseTopkDecoderCossimFeaturesInner`
        """
        model = UtilSaeTopkByDecoderCossimPost200ResponseTopkDecoderCossimFeaturesInner()
        if include_optional:
            return UtilSaeTopkByDecoderCossimPost200ResponseTopkDecoderCossimFeaturesInner(
                feature = memicos_inference_client.models.np_feature.NPFeature(
                    model = 'gpt2-small', 
                    source = '0-res-jb', 
                    index = 14057, ),
                cosine_similarity = 1.337
            )
        else:
            return UtilSaeTopkByDecoderCossimPost200ResponseTopkDecoderCossimFeaturesInner(
        )
        """

    def testUtilSaeTopkByDecoderCossimPost200ResponseTopkDecoderCossimFeaturesInner(self):
        """Test UtilSaeTopkByDecoderCossimPost200ResponseTopkDecoderCossimFeaturesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
