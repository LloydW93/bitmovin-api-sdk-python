# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.closed_captions_media_info import ClosedCaptionsMediaInfo
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.manifests.hls.media.closedCaptions.closed_captions_media_info_list_query_params import ClosedCaptionsMediaInfoListQueryParams


class ClosedCaptionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ClosedCaptionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, closed_captions_media_info, **kwargs):
        """Add Closed Captions Media"""

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/media/closed-captions',
            closed_captions_media_info,
            path_params={'manifest_id': manifest_id},
            type=ClosedCaptionsMediaInfo,
            **kwargs
        )

    def delete(self, manifest_id, media_id, **kwargs):
        """Delete Closed Captions Media"""

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/media/closed-captions/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, media_id, **kwargs):
        """Closed Captions Media Details"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/closed-captions/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=ClosedCaptionsMediaInfo,
            **kwargs
        )

    def list(self, manifest_id, query_params: ClosedCaptionsMediaInfoListQueryParams = None, **kwargs):
        """List all Closed Captions Media"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/closed-captions',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=ClosedCaptionsMediaInfo,
            **kwargs
        )