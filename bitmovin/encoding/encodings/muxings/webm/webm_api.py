# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.webm_muxing import WebmMuxing
from bitmovin.encoding.encodings.muxings.webm.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.muxings.webm.drm.drm_api import DrmApi
from bitmovin.encoding.encodings.muxings.webm.webm_muxing_list_query_params import WebmMuxingListQueryParams


class WebmApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(WebmApi, self).__init__(
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

        self.drm = DrmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, webm_muxing, **kwargs):
        """Add WebM Segment Muxing"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/webm',
            webm_muxing,
            path_params={'encoding_id': encoding_id},
            type=WebmMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        """Delete WebM Muxing"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/webm/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        """WebM Segment Muxing Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/webm/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=WebmMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params: WebmMuxingListQueryParams = None, **kwargs):
        """List WebM Segment Muxings"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/webm',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=WebmMuxing,
            **kwargs
        )
