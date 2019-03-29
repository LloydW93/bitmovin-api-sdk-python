# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.aspera_input import AsperaInput
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.inputs.aspera.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.inputs.aspera.aspera_input_list_query_params import AsperaInputListQueryParams


class AsperaApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AsperaApi, self).__init__(
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

    def create(self, aspera_input, **kwargs):
        """Create Aspera Input"""

        return self.api_client.post(
            '/encoding/inputs/aspera',
            aspera_input,
            type=AsperaInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete Aspera Input"""

        return self.api_client.delete(
            '/encoding/inputs/aspera/{input_id}',
            path_params={'input_id': input_id},
            type=AsperaInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """Aspera Input Details"""

        return self.api_client.get(
            '/encoding/inputs/aspera/{input_id}',
            path_params={'input_id': input_id},
            type=AsperaInput,
            **kwargs
        )

    def list(self, query_params: AsperaInputListQueryParams = None, **kwargs):
        """List Aspera Inputs"""

        return self.api_client.get(
            '/encoding/inputs/aspera',
            query_params=query_params,
            pagination_response=True,
            type=AsperaInput,
            **kwargs
        )
