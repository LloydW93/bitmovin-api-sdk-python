# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.rotate_filter import RotateFilter
from bitmovin.encoding.filters.rotate.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.filters.rotate.rotate_filter_list_query_params import RotateFilterListQueryParams


class RotateApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(RotateApi, self).__init__(
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

    def create(self, rotate_filter, **kwargs):
        """Create Rotate Filter"""

        return self.api_client.post(
            '/encoding/filters/rotate',
            rotate_filter,
            type=RotateFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Rotate Filter"""

        return self.api_client.delete(
            '/encoding/filters/rotate/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Rotate Filter Details"""

        return self.api_client.get(
            '/encoding/filters/rotate/{filter_id}',
            path_params={'filter_id': filter_id},
            type=RotateFilter,
            **kwargs
        )

    def list(self, query_params: RotateFilterListQueryParams = None, **kwargs):
        """List Rotate Filters"""

        return self.api_client.get(
            '/encoding/filters/rotate',
            query_params=query_params,
            pagination_response=True,
            type=RotateFilter,
            **kwargs
        )