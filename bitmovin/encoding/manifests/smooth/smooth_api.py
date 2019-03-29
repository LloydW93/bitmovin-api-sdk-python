# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.smooth_streaming_manifest import SmoothStreamingManifest
from bitmovin.models.task import Task
from bitmovin.encoding.manifests.smooth.default.default_api import DefaultApi
from bitmovin.encoding.manifests.smooth.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.manifests.smooth.representations.representations_api import RepresentationsApi
from bitmovin.encoding.manifests.smooth.contentprotection.contentprotection_api import ContentprotectionApi
from bitmovin.encoding.manifests.smooth.smooth_streaming_manifest_list_query_params import SmoothStreamingManifestListQueryParams


class SmoothApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(SmoothApi, self).__init__(
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

        self.representations = RepresentationsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.contentprotection = ContentprotectionApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, smooth_streaming_manifest, **kwargs):
        """Create Smooth Streaming Manifest"""

        return self.api_client.post(
            '/encoding/manifests/smooth',
            smooth_streaming_manifest,
            type=SmoothStreamingManifest,
            **kwargs
        )

    def delete(self, manifest_id, **kwargs):
        """Delete Smooth Streaming Manifest"""

        return self.api_client.delete(
            '/encoding/manifests/smooth/{manifest_id}',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, **kwargs):
        """Smooth Streaming Manifest Details"""

        return self.api_client.get(
            '/encoding/manifests/smooth/{manifest_id}',
            path_params={'manifest_id': manifest_id},
            type=SmoothStreamingManifest,
            **kwargs
        )

    def list(self, query_params: SmoothStreamingManifestListQueryParams = None, **kwargs):
        """List Smooth Streaming Manifests"""

        return self.api_client.get(
            '/encoding/manifests/smooth',
            query_params=query_params,
            pagination_response=True,
            type=SmoothStreamingManifest,
            **kwargs
        )

    def start(self, manifest_id, **kwargs):
        """Start Smooth Streaming Manifest Creation"""

        return self.api_client.post(
            '/encoding/manifests/smooth/{manifest_id}/start',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )

    def status(self, manifest_id, **kwargs):
        """Smooth Streaming Manifest Creation Status"""

        return self.api_client.get(
            '/encoding/manifests/smooth/{manifest_id}/status',
            path_params={'manifest_id': manifest_id},
            type=Task,
            **kwargs
        )

    def stop(self, manifest_id, **kwargs):
        """Stop Smooth Streaming Manifest Creation"""

        return self.api_client.post(
            '/encoding/manifests/smooth/{manifest_id}/stop',
            path_params={'manifest_id': manifest_id},
            type=BitmovinResponse,
            **kwargs
        )