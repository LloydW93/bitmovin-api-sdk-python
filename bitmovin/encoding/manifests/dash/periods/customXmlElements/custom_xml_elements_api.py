# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.custom_xml_element import CustomXmlElement
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.manifests.dash.periods.customXmlElements.custom_xml_element_list_query_params import CustomXmlElementListQueryParams


class CustomXmlElementsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(CustomXmlElementsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period_id, custom_xml_element, **kwargs):
        """Add Custom XML Element to Period"""

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/custom-xml-elements',
            custom_xml_element,
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            type=CustomXmlElement,
            **kwargs
        )

    def delete(self, manifest_id, period_id, custom_xml_element_id, **kwargs):
        """Delete Custom XML Element"""

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/custom-xml-elements/{custom_xml_element_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'custom_xml_element_id': custom_xml_element_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, custom_xml_element_id, **kwargs):
        """Custom XML Element Details"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/custom-xml-elements/{custom_xml_element_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'custom_xml_element_id': custom_xml_element_id},
            type=CustomXmlElement,
            **kwargs
        )

    def list(self, manifest_id, period_id, query_params: CustomXmlElementListQueryParams = None, **kwargs):
        """List all Custom XML Elements of Period"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/custom-xml-elements',
            path_params={'manifest_id': manifest_id, 'period_id': period_id},
            query_params=query_params,
            pagination_response=True,
            type=CustomXmlElement,
            **kwargs
        )
