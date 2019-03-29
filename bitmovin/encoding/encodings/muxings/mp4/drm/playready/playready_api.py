# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.play_ready_drm import PlayReadyDrm
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.muxings.mp4.drm.playready.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.muxings.mp4.drm.playready.play_ready_drm_list_query_params import PlayReadyDrmListQueryParams


class PlayreadyApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(PlayreadyApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, play_ready_drm, **kwargs):
        """Add PlayReady DRM to MP4"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/playready',
            play_ready_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=PlayReadyDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        """Delete PlayReady DRM from MP4"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/playready/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        """PlayReady DRM Details of MP4"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/playready/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=PlayReadyDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params: PlayReadyDrmListQueryParams = None, **kwargs):
        """List PlayReady DRMs of MP4"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/mp4/{muxing_id}/drm/playready',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=PlayReadyDrm,
            **kwargs
        )
