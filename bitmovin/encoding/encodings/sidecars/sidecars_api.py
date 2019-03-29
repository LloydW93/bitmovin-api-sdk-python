# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.sidecar_file import SidecarFile
from bitmovin.encoding.encodings.sidecars.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.sidecars.sidecar_file_list_query_params import SidecarFileListQueryParams


class SidecarsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(SidecarsApi, self).__init__(
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

    def create(self, encoding_id, sidecar_file, **kwargs):
        """Add Sidecar"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/sidecars',
            sidecar_file,
            path_params={'encoding_id': encoding_id},
            type=SidecarFile,
            **kwargs
        )

    def delete(self, encoding_id, sidecar_id, **kwargs):
        """Delete Sidecar"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/sidecars/{sidecar_id}',
            path_params={'encoding_id': encoding_id, 'sidecar_id': sidecar_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, sidecar_id, **kwargs):
        """Sidecar Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/sidecars/{sidecar_id}',
            path_params={'encoding_id': encoding_id, 'sidecar_id': sidecar_id},
            type=SidecarFile,
            **kwargs
        )

    def list(self, encoding_id, query_params: SidecarFileListQueryParams = None, **kwargs):
        """List Sidecars"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/sidecars',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=SidecarFile,
            **kwargs
        )