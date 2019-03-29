# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.watermark_filter import WatermarkFilter
from bitmovin.encoding.filters.watermark.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.filters.watermark.watermark_filter_list_query_params import WatermarkFilterListQueryParams


class WatermarkApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(WatermarkApi, self).__init__(
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

    def create(self, watermark_filter, **kwargs):
        """Create Watermark Filter"""

        return self.api_client.post(
            '/encoding/filters/watermark',
            watermark_filter,
            type=WatermarkFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Watermark Filter"""

        return self.api_client.delete(
            '/encoding/filters/watermark/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Watermark Filter Details"""

        return self.api_client.get(
            '/encoding/filters/watermark/{filter_id}',
            path_params={'filter_id': filter_id},
            type=WatermarkFilter,
            **kwargs
        )

    def list(self, query_params: WatermarkFilterListQueryParams = None, **kwargs):
        """List Watermark Filters"""

        return self.api_client.get(
            '/encoding/filters/watermark',
            query_params=query_params,
            pagination_response=True,
            type=WatermarkFilter,
            **kwargs
        )