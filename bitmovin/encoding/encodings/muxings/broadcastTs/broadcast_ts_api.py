# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.broadcast_ts_muxing import BroadcastTsMuxing
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.muxings.broadcastTs.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.muxings.broadcastTs.information.information_api import InformationApi
from bitmovin.encoding.encodings.muxings.broadcastTs.broadcast_ts_muxing_list_query_params import BroadcastTsMuxingListQueryParams


class BroadcastTsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(BroadcastTsApi, self).__init__(
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

    def create(self, encoding_id, broadcast_ts_muxing, **kwargs):
        """Add Broadcast TS Muxing"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/broadcast-ts',
            broadcast_ts_muxing,
            path_params={'encoding_id': encoding_id},
            type=BroadcastTsMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        """Delete Broadcast TS Muxing"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/broadcast-ts/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        """Broadcast TS Muxing Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/broadcast-ts/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BroadcastTsMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params: BroadcastTsMuxingListQueryParams = None, **kwargs):
        """List Broadcast TS Muxings"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/broadcast-ts',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=BroadcastTsMuxing,
            **kwargs
        )