# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.audio_adaptation_set import AudioAdaptationSet
from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.manifests.dash.periods.adaptationsets.audio.audio_adaptation_set_list_query_params import AudioAdaptationSetListQueryParams


class AudioApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AudioApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period_id, audio_adaptation_set, **kwargs):
        """Add Audio AdaptationSet"""

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/audio',
            audio_adaptation_set,
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            type=AudioAdaptationSet,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, **kwargs):
        """Delete Audio AdaptationSet"""

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/audio/{adaptationset_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, **kwargs):
        """Audio AdaptationSet Details"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/audio/{adaptationset_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=AudioAdaptationSet,
            **kwargs
        )

    def list(self, manifest_id, period_id, query_params: AudioAdaptationSetListQueryParams = None, **kwargs):
        """List all Audio AdaptationSets"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/audio',
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            query_params=query_params,
            pagination_response=True,
            type=AudioAdaptationSet,
            **kwargs
        )