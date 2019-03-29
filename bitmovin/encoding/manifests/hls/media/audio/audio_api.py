# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.audio_media_info import AudioMediaInfo
from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.manifests.hls.media.audio.audio_media_info_list_query_params import AudioMediaInfoListQueryParams


class AudioApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AudioApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, audio_media_info, **kwargs):
        """Add Audio Media"""

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/media/audio',
            audio_media_info,
            path_params={'manifest_id': manifest_id},
            type=AudioMediaInfo,
            **kwargs
        )

    def delete(self, manifest_id, media_id, **kwargs):
        """Delete Audio Media"""

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}/media/audio/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, media_id, **kwargs):
        """Audio Media Details"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/audio/{media_id}',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=AudioMediaInfo,
            **kwargs
        )

    def list(self, manifest_id, query_params: AudioMediaInfoListQueryParams = None, **kwargs):
        """List all Audio Media"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/audio',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=AudioMediaInfo,
            **kwargs
        )