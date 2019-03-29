# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.mp3_audio_configuration import Mp3AudioConfiguration
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.configurations.audio.mp3.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.configurations.audio.mp3.mp3_audio_configuration_list_query_params import Mp3AudioConfigurationListQueryParams


class Mp3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(Mp3Api, self).__init__(
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

    def create(self, mp3_audio_configuration, **kwargs):
        """Create MP3 Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/audio/mp3',
            mp3_audio_configuration,
            type=Mp3AudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete MP3 Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/audio/mp3/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """MP3 Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/audio/mp3/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Mp3AudioConfiguration,
            **kwargs
        )

    def list(self, query_params: Mp3AudioConfigurationListQueryParams = None, **kwargs):
        """List MP3 Configurations"""

        return self.api_client.get(
            '/encoding/configurations/audio/mp3',
            query_params=query_params,
            pagination_response=True,
            type=Mp3AudioConfiguration,
            **kwargs
        )