# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.https_input import HttpsInput
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.inputs.https.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.inputs.https.https_input_list_query_params import HttpsInputListQueryParams


class HttpsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(HttpsApi, self).__init__(
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

    def create(self, https_input, **kwargs):
        """Create HTTPS Input"""

        return self.api_client.post(
            '/encoding/inputs/https',
            https_input,
            type=HttpsInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete HTTPS Input"""

        return self.api_client.delete(
            '/encoding/inputs/https/{input_id}',
            path_params={'input_id': input_id},
            type=HttpsInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """HTTPS Input Details"""

        return self.api_client.get(
            '/encoding/inputs/https/{input_id}',
            path_params={'input_id': input_id},
            type=HttpsInput,
            **kwargs
        )

    def list(self, query_params: HttpsInputListQueryParams = None, **kwargs):
        """List HTTPS Inputs"""

        return self.api_client.get(
            '/encoding/inputs/https',
            query_params=query_params,
            pagination_response=True,
            type=HttpsInput,
            **kwargs
        )