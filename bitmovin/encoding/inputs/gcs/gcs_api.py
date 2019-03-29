# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.gcs_input import GcsInput
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.inputs.gcs.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.inputs.gcs.gcs_input_list_query_params import GcsInputListQueryParams


class GcsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(GcsApi, self).__init__(
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

    def create(self, gcs_input, **kwargs):
        """Create GCS Input"""

        return self.api_client.post(
            '/encoding/inputs/gcs',
            gcs_input,
            type=GcsInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete GCS Input"""

        return self.api_client.delete(
            '/encoding/inputs/gcs/{input_id}',
            path_params={'input_id': input_id},
            type=GcsInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """GCS Input Details"""

        return self.api_client.get(
            '/encoding/inputs/gcs/{input_id}',
            path_params={'input_id': input_id},
            type=GcsInput,
            **kwargs
        )

    def list(self, query_params: GcsInputListQueryParams = None, **kwargs):
        """List GCS Inputs"""

        return self.api_client.get(
            '/encoding/inputs/gcs',
            query_params=query_params,
            pagination_response=True,
            type=GcsInput,
            **kwargs
        )