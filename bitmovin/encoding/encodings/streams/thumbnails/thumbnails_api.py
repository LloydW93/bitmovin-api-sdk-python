# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.thumbnail import Thumbnail
from bitmovin.encoding.encodings.streams.thumbnails.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.streams.thumbnails.thumbnail_list_query_params import ThumbnailListQueryParams


class ThumbnailsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ThumbnailsApi, self).__init__(
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

    def create(self, encoding_id, stream_id, thumbnail, **kwargs):
        """Add Thumbnail"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/thumbnails',
            thumbnail,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=Thumbnail,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, thumbnail_id, **kwargs):
        """Delete Thumbnail"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/thumbnails/{thumbnail_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'thumbnail_id': thumbnail_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, thumbnail_id, **kwargs):
        """Thumbnail Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/thumbnails/{thumbnail_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'thumbnail_id': thumbnail_id},
            type=Thumbnail,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params: ThumbnailListQueryParams = None, **kwargs):
        """List Thumbnails"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/thumbnails',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=Thumbnail,
            **kwargs
        )