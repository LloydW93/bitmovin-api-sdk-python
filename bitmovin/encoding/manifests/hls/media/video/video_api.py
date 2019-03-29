# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.standard_media_info import StandardMediaInfo
from bitmovin.models.video_media_info import VideoMediaInfo
from bitmovin.encoding.manifests.hls.media.video.iframe.iframe_api import IframeApi
from bitmovin.encoding.manifests.hls.media.video.video_media_info_list_query_params import VideoMediaInfoListQueryParams


class VideoApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(VideoApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.iframe = IframeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, video_media_info, **kwargs):
        """Add Video Media"""

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/media/video',
            video_media_info,
            path_params={'manifest_id': manifest_id},
            type=VideoMediaInfo,
            **kwargs
        )

    def delete(self, manifest_id, media_id, **kwargs):
        """Delete Video Media"""

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/media/video/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, media_id, **kwargs):
        """Video Media Details"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/video/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=VideoMediaInfo,
            **kwargs
        )

    def list(self, manifest_id, query_params: VideoMediaInfoListQueryParams = None, **kwargs):
        """List all Video Media"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/video',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=VideoMediaInfo,
            **kwargs
        )