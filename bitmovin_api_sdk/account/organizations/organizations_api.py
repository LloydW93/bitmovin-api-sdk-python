# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.organization import Organization
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.account.organizations.groups.groups_api import GroupsApi


class OrganizationsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(OrganizationsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.groups = GroupsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, organization, **kwargs):
        # type: (Organization, dict) -> Organization
        """Add Organization

        :param organization: Orgnaization Details
        :type organization: Organization, required
        :return: Orgnaization Details
        :rtype: Organization
        """

        return self.api_client.post(
            '/account/organizations',
            organization,
            type=Organization,
            **kwargs
        )

    def delete(self, organization_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Organization

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :return: Id of the Organization
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/account/organizations/{organization_id}',
            path_params={'organization_id': organization_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, organization_id, **kwargs):
        # type: (string_types, dict) -> Organization
        """Organization Details

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :return: Organization details
        :rtype: Organization
        """

        return self.api_client.get(
            '/account/organizations/{organization_id}',
            path_params={'organization_id': organization_id},
            type=Organization,
            **kwargs
        )

    def list(self, **kwargs):
        # type: (dict) -> Organization
        """List Organizations

        :return: Service specific result
        :rtype: Organization
        """

        return self.api_client.get(
            '/account/organizations',
            pagination_response=True,
            type=Organization,
            **kwargs
        )