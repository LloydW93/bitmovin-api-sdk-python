# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.stream_infos import StreamInfos
from bitmovin.encoding.statistics.encodings.liveStatistics.streams.stream_infos_list_query_params import StreamInfosListQueryParams


class StreamsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(StreamsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, query_params: StreamInfosListQueryParams = None, **kwargs):
        """List Stream Infos of Live Statistics from an Encoding"""

        return self.api_client.get(
            '/encoding/statistics/encodings/{encoding_id}/live-statistics/streams',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=StreamInfos,
            **kwargs
        )