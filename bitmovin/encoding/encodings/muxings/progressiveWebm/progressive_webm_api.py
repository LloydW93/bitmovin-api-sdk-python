# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.progressive_webm_muxing import ProgressiveWebmMuxing
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.muxings.progressiveWebm.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.muxings.progressiveWebm.information.information_api import InformationApi
from bitmovin.encoding.encodings.muxings.progressiveWebm.progressive_webm_muxing_list_query_params import ProgressiveWebmMuxingListQueryParams


class ProgressiveWebmApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ProgressiveWebmApi, self).__init__(
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

        self.information = InformationApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, progressive_webm_muxing, **kwargs):
        """Add Progressive WebM Muxing"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/progressive-webm',
            progressive_webm_muxing,
            path_params={'encoding_id': encoding_id},
            type=ProgressiveWebmMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        """Delete Progressive WebM Muxing"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/progressive-webm/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        """Progressive WebM Muxing Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-webm/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=ProgressiveWebmMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params: ProgressiveWebmMuxingListQueryParams = None, **kwargs):
        """List Progressive WebM Muxings"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-webm',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ProgressiveWebmMuxing,
            **kwargs
        )
