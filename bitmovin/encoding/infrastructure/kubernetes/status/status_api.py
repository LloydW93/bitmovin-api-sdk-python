# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_error import ResponseError


class StatusApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(StatusApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, infrastructure_id, **kwargs):
        """Kubernetes Cluster Status"""

        self.api_client.get(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/status',
            path_params={'infrastructure_id': infrastructure_id},
            **kwargs
        )