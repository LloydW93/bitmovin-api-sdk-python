# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.basic_input_stream import BasicInputStream
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.inputStreams.type.type_api import TypeApi
from bitmovin.encoding.encodings.inputStreams.audioMix.audio_mix_api import AudioMixApi
from bitmovin.encoding.encodings.inputStreams.ingest.ingest_api import IngestApi
from bitmovin.encoding.encodings.inputStreams.concatenation.concatenation_api import ConcatenationApi
from bitmovin.encoding.encodings.inputStreams.trimming.trimming_api import TrimmingApi
from bitmovin.encoding.encodings.inputStreams.basic_input_stream_list_query_params import BasicInputStreamListQueryParams


class InputStreamsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(InputStreamsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.type = TypeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.audioMix = AudioMixApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.ingest = IngestApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.concatenation = ConcatenationApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.trimming = TrimmingApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        """Input Stream Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BasicInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params: BasicInputStreamListQueryParams = None, **kwargs):
        """List All Input Streams"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=BasicInputStream,
            **kwargs
        )
