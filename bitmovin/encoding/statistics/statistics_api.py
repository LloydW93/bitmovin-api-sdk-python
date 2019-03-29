# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.statistics import Statistics
from bitmovin.encoding.statistics.daily.daily_api import DailyApi
from bitmovin.encoding.statistics.encodings.encodings_api import EncodingsApi
from bitmovin.encoding.statistics.labels.labels_api import LabelsApi
from bitmovin.encoding.statistics.statistics_list_query_params import StatisticsListQueryParams


class StatisticsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(StatisticsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.daily = DailyApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.encodings = EncodingsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.labels = LabelsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, **kwargs):
        """Show Overall Statistics"""

        return self.api_client.get(
            '/encoding/statistics',
            type=Statistics,
            **kwargs
        )

    def list(self, _from, to, query_params: StatisticsListQueryParams = None, **kwargs):
        """Show Overall Statistics Within Specific Dates"""

        return self.api_client.get(
            '/encoding/statistics/{from}/{to}',
            path_params={'from': _from, 'to': to},
            query_params=query_params,
            pagination_response=True,
            type=Statistics,
            **kwargs
        )