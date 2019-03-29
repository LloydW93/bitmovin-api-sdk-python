# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.analytics_query_request import AnalyticsQueryRequest
from bitmovin.models.analytics_response import AnalyticsResponse
from bitmovin.models.analytics_variance_query_request import AnalyticsVarianceQueryRequest
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError


class VarianceApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(VarianceApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, analytics_variance_query_request, **kwargs):
        """Variance"""

        return self.api_client.post(
            '/analytics/queries/variance',
            analytics_variance_query_request,
            type=AnalyticsResponse,
            **kwargs
        )