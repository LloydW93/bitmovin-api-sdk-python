# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.clear_key_drm import ClearKeyDrm
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.muxings.fmp4.drm.clearkey.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.muxings.fmp4.drm.clearkey.clear_key_drm_list_query_params import ClearKeyDrmListQueryParams


class ClearkeyApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ClearkeyApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, clear_key_drm, **kwargs):
        """Add ClearKey DRM to fMP4"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/clearkey',
            clear_key_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=ClearKeyDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        """Delete ClearKey DRM from fMP4"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/clearkey/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        """ClearKey DRM Details of fMP4"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/clearkey/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=ClearKeyDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params: ClearKeyDrmListQueryParams = None, **kwargs):
        """List ClearKey DRMs of fMP4"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}/drm/clearkey',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=ClearKeyDrm,
            **kwargs
        )