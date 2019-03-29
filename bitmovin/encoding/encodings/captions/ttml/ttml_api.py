# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.ttml_extract import TtmlExtract
from bitmovin.encoding.encodings.captions.ttml.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.captions.ttml.ttml_extract_list_query_params import TtmlExtractListQueryParams


class TtmlApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(TtmlApi, self).__init__(
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

    def create(self, encoding_id, ttml_extract, **kwargs):
        """Extract TTML Captions"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/captions/ttml',
            ttml_extract,
            path_params={'encoding_id': encoding_id},
            type=TtmlExtract,
            **kwargs
        )

    def delete(self, encoding_id, captions_id, **kwargs):
        """Delete TTML Extract Captions"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/captions/ttml/{captions_id}',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=TtmlExtract,
            **kwargs
        )

    def get(self, encoding_id, captions_id, **kwargs):
        """TTML Extract Captions Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/ttml/{captions_id}',
            path_params={'encoding_id': encoding_id, 'captions_id': captions_id},
            type=TtmlExtract,
            **kwargs
        )

    def list(self, encoding_id, query_params: TtmlExtractListQueryParams = None, **kwargs):
        """List TTML Extract Captions"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/captions/ttml',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=TtmlExtract,
            **kwargs
        )
