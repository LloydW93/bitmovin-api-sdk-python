# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.player_license import PlayerLicense
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.player.licenses.domains.domains_api import DomainsApi
from bitmovin.player.licenses.thirdPartyLicensing.third_party_licensing_api import ThirdPartyLicensingApi
from bitmovin.player.licenses.player_license_list_query_params import PlayerLicenseListQueryParams


class LicensesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(LicensesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.domains = DomainsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.thirdPartyLicensing = ThirdPartyLicensingApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, license_id, **kwargs):
        """Get License"""

        return self.api_client.get(
            '/player/licenses/{license_id}',
            path_params={'license_id': license_id},
            type=PlayerLicense,
            **kwargs
        )

    def list(self, query_params: PlayerLicenseListQueryParams = None, **kwargs):
        """List Player Licenses"""

        return self.api_client.get(
            '/player/licenses',
            query_params=query_params,
            pagination_response=True,
            type=PlayerLicense,
            **kwargs
        )