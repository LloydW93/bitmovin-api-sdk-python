# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.crop_filter import CropFilter
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.filters.crop.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.filters.crop.crop_filter_list_query_params import CropFilterListQueryParams


class CropApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(CropApi, self).__init__(
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

    def create(self, crop_filter, **kwargs):
        """Create Crop Filter"""

        return self.api_client.post(
            '/encoding/filters/crop',
            crop_filter,
            type=CropFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Crop Filter"""

        return self.api_client.delete(
            '/encoding/filters/crop/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Crop Filter Details"""

        return self.api_client.get(
            '/encoding/filters/crop/{filter_id}',
            path_params={'filter_id': filter_id},
            type=CropFilter,
            **kwargs
        )

    def list(self, query_params: CropFilterListQueryParams = None, **kwargs):
        """List Crop Filters"""

        return self.api_client.get(
            '/encoding/filters/crop',
            query_params=query_params,
            pagination_response=True,
            type=CropFilter,
            **kwargs
        )