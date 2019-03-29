# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.http_input import HttpInput
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.inputs.http.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.inputs.http.http_input_list_query_params import HttpInputListQueryParams


class HttpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(HttpApi, self).__init__(
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

    def create(self, http_input, **kwargs):
        """Create HTTP Input"""

        return self.api_client.post(
            '/encoding/inputs/http',
            http_input,
            type=HttpInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete HTTP Input"""

        return self.api_client.delete(
            '/encoding/inputs/http/{input_id}',
            path_params={'input_id': input_id},
            type=HttpInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """HTTP Input Details"""

        return self.api_client.get(
            '/encoding/inputs/http/{input_id}',
            path_params={'input_id': input_id},
            type=HttpInput,
            **kwargs
        )

    def list(self, query_params: HttpInputListQueryParams = None, **kwargs):
        """List HTTP Inputs"""

        return self.api_client.get(
            '/encoding/inputs/http',
            query_params=query_params,
            pagination_response=True,
            type=HttpInput,
            **kwargs
        )