# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.smooth_streaming_representation import SmoothStreamingRepresentation
from bitmovin.encoding.manifests.smooth.representations.mp4.smooth_streaming_representation_list_query_params import SmoothStreamingRepresentationListQueryParams


class Mp4Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(Mp4Api, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, smooth_streaming_representation, **kwargs):
        """Add MP4 Representation to Smooth Streaming Manifest"""

        return self.api_client.post(
            '/encoding/manifests/smooth/{manifest_id}/representations/mp4',
            smooth_streaming_representation,
            path_params={'manifest_id': manifest_id},
            type=SmoothStreamingRepresentation,
            **kwargs
        )

    def delete(self, manifest_id, representation_id, **kwargs):
        """Delete Smooth Streaming MP4 Representation"""

        return self.api_client.delete(
            '/encoding/manifests/smooth/{manifest_id}/representations/mp4/{representation_id}',
            path_params={'manifest_id': manifest_id, 'representation_id': representation_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, representation_id, **kwargs):
        """Smooth Streaming MP4 Representation Details"""

        return self.api_client.get(
            '/encoding/manifests/smooth/{manifest_id}/representations/mp4/{representation_id}',
            path_params={'manifest_id': manifest_id, 'representation_id': representation_id},
            type=SmoothStreamingRepresentation,
            **kwargs
        )

    def list(self, manifest_id, query_params: SmoothStreamingRepresentationListQueryParams = None, **kwargs):
        """List MP4 Representation"""

        return self.api_client.get(
            '/encoding/manifests/smooth/{manifest_id}/representations/mp4',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=SmoothStreamingRepresentation,
            **kwargs
        )
