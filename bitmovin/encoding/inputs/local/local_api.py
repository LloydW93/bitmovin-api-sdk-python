# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.local_input import LocalInput
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.inputs.local.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.inputs.local.local_input_list_query_params import LocalInputListQueryParams


class LocalApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(LocalApi, self).__init__(
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

    def create(self, local_input, **kwargs):
        """Create Local Input"""

        return self.api_client.post(
            '/encoding/inputs/local',
            local_input,
            type=LocalInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete Local Input"""

        return self.api_client.delete(
            '/encoding/inputs/local/{input_id}',
            path_params={'input_id': input_id},
            type=LocalInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """Local Input Details"""

        return self.api_client.get(
            '/encoding/inputs/local/{input_id}',
            path_params={'input_id': input_id},
            type=LocalInput,
            **kwargs
        )

    def list(self, query_params: LocalInputListQueryParams = None, **kwargs):
        """List Local Inputs"""

        return self.api_client.get(
            '/encoding/inputs/local',
            query_params=query_params,
            pagination_response=True,
            type=LocalInput,
            **kwargs
        )