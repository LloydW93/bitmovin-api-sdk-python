# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.s3_input import S3Input
from bitmovin.encoding.inputs.s3.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.inputs.s3.s3_input_list_query_params import S3InputListQueryParams


class S3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(S3Api, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, s3_input, **kwargs):
        """Create S3 Input"""

        return self.api_client.post(
            '/encoding/inputs/s3',
            s3_input,
            type=S3Input,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete S3 Input"""

        return self.api_client.delete(
            '/encoding/inputs/s3/{input_id}',
            path_params={'input_id': input_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """S3 Input Details"""

        return self.api_client.get(
            '/encoding/inputs/s3/{input_id}',
            path_params={'input_id': input_id},
            type=S3Input,
            **kwargs
        )

    def list(self, query_params: S3InputListQueryParams = None, **kwargs):
        """List S3 Inputs"""

        return self.api_client.get(
            '/encoding/inputs/s3',
            query_params=query_params,
            pagination_response=True,
            type=S3Input,
            **kwargs
        )