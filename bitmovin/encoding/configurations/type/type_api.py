# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.codec_config_type_response import CodecConfigTypeResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError


class TypeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(TypeApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, configuration_id, **kwargs):
        """Get Codec Configuration Type"""

        return self.api_client.get(
            '/encoding/configurations/{configuration_id}/type',
            path_params={'configuration_id': configuration_id},
            type=CodecConfigTypeResponse,
            **kwargs
        )