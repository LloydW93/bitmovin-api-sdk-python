# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.domain import Domain
from bitmovin.models.domain_list import DomainList
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError


class DomainsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DomainsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, license_id, domain, **kwargs):
        """Add Domain"""

        return self.api_client.post(
            '/analytics/licenses/{license_id}/domains',
            domain,
            path_params={'license_id': license_id},
            type=Domain,
            **kwargs
        )

    def delete(self, license_id, domain_id, **kwargs):
        """Delete Domain"""

        return self.api_client.delete(
            '/analytics/licenses/{license_id}/domains/{domain_id}',
            path_params={'license_id': license_id, 'domain_id': domain_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, license_id, **kwargs):
        """List License Domains"""

        return self.api_client.get(
            '/analytics/licenses/{license_id}/domains',
            path_params={'license_id': license_id},
            type=DomainList,
            **kwargs
        )