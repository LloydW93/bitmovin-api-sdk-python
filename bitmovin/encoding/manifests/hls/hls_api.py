# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.hls_manifest import HlsManifest
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.task import Task
from bitmovin.encoding.manifests.hls.default.default_api import DefaultApi
from bitmovin.encoding.manifests.hls.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.manifests.hls.streams.streams_api import StreamsApi
from bitmovin.encoding.manifests.hls.media.media_api import MediaApi
from bitmovin.encoding.manifests.hls.hls_manifest_list_query_params import HlsManifestListQueryParams


class HlsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(HlsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.default = DefaultApi(
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

        self.streams = StreamsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.media = MediaApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, hls_manifest, **kwargs):
        """Create HLS Manifest"""

        return self.api_client.post(
            '/encoding/manifests/hls',
            hls_manifest,
            type=HlsManifest,
            **kwargs
        )

    def delete(self, manifest_id, **kwargs):
        """Delete HLS Manifest"""

        return self.api_client.delete(
            '/encoding/manifests/hls/{manifest_id}',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, **kwargs):
        """HLS Manifest Details"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}',
            path_params={'manifest_id': manifest_id},
            type=HlsManifest,
            **kwargs
        )

    def list(self, query_params: HlsManifestListQueryParams = None, **kwargs):
        """List HLS Manifests"""

        return self.api_client.get(
            '/encoding/manifests/hls',
            query_params=query_params,
            pagination_response=True,
            type=HlsManifest,
            **kwargs
        )

    def start(self, manifest_id, **kwargs):
        """Start HLS Manifest Creation"""

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/start',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )

    def status(self, manifest_id, **kwargs):
        """HLS Manifest Creation Status"""

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/status',
            path_params={'manifest_id': manifest_id},
            type=Task,
            **kwargs
        )

    def stop(self, manifest_id, **kwargs):
        """Stop HLS Manifest Creation"""

        return self.api_client.post(
            '/encoding/manifests/hls/{manifest_id}/stop',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )