# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.h264_picture_timing_trimming_input_stream import H264PictureTimingTrimmingInputStream
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.inputStreams.trimming.h264PictureTiming.h264_picture_timing_trimming_input_stream_list_query_params import H264PictureTimingTrimmingInputStreamListQueryParams


class H264PictureTimingApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(H264PictureTimingApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, h264_picture_timing_trimming_input_stream, **kwargs):
        """Add H264 Picture Timing Trimming Input Stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/h264-picture-timing',
            h264_picture_timing_trimming_input_stream,
            path_params={'encoding_id': encoding_id},
            type=H264PictureTimingTrimmingInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        """Delete H264 Picture Timing Trimming Input Stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/h264-picture-timing/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        """H264 Picture Timing Trimming Input Stream Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/h264-picture-timing/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=H264PictureTimingTrimmingInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params: H264PictureTimingTrimmingInputStreamListQueryParams = None, **kwargs):
        """List H264 Picture Timing Trimming Input Streams"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/h264-picture-timing',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=H264PictureTimingTrimmingInputStream,
            **kwargs
        )