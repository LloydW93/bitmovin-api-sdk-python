# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.live_encoding_stats_event import LiveEncodingStatsEvent
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.statistics.encodings.liveStatistics.events.live_encoding_stats_event_list_query_params import LiveEncodingStatsEventListQueryParams


class EventsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(EventsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, query_params: LiveEncodingStatsEventListQueryParams = None, **kwargs):
        """List Events of Live Statistics from an Encoding"""

        return self.api_client.get(
            '/encoding/statistics/encodings/{encoding_id}/live-statistics/events',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=LiveEncodingStatsEvent,
            **kwargs
        )