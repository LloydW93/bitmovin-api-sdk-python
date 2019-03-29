# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.fair_play_drm import FairPlayDrm
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.muxings.ts.drm.fairplay.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.muxings.ts.drm.fairplay.fair_play_drm_list_query_params import FairPlayDrmListQueryParams


class FairplayApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(FairplayApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, fair_play_drm, **kwargs):
        """Add FairPlay DRM to TS Segment"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/drm/fairplay',
            fair_play_drm,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=FairPlayDrm,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, drm_id, **kwargs):
        """Delete FairPlay DRM from TS Segment"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/drm/fairplay/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, drm_id, **kwargs):
        """FairPlay DRM Details of TS Segment"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/drm/fairplay/{drm_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'drm_id': drm_id},
            type=FairPlayDrm,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params: FairPlayDrmListQueryParams = None, **kwargs):
        """List FairPlay DRMs of TS Segment"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}/drm/fairplay',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=FairPlayDrm,
            **kwargs
        )