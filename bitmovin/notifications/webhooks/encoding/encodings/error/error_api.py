# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.webhook import Webhook
from bitmovin.notifications.webhooks.encoding.encodings.error.customdata.customdata_api import CustomdataApi
from bitmovin.notifications.webhooks.encoding.encodings.error.webhook_list_query_params import WebhookListQueryParams
from bitmovin.notifications.webhooks.encoding.encodings.error.webhook_list_by_encoding_id_query_params import WebhookListByEncodingIdQueryParams


class ErrorApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ErrorApi, self).__init__(
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

    def create(self, webhook, **kwargs):
        """Add Encoding Error Webhook"""

        return self.api_client.post(
            '/notifications/webhooks/encoding/encodings/error',
            webhook,
            type=Webhook,
            **kwargs
        )

    def createbyEncodingId(self, encoding_id, webhook, **kwargs):
        """Add Encoding Error Webhook for specific Encoding Resource"""

        return self.api_client.post(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/error',
            webhook,
            path_params={'encoding_id': encoding_id},
            type=Webhook,
            **kwargs
        )

    def deleteByEncodingIdAndWebhookId(self, encoding_id, webhook_id, **kwargs):
        """Delete Encoding Error Webhook for specific Encoding Resource"""

        return self.api_client.delete(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/error/{webhook_id}',
            path_params={'encoding_id': encoding_id, 'webhook_id': webhook_id},
            type=BitmovinResponse,
            **kwargs
        )

    def deleteByWebhookId(self, webhook_id, **kwargs):
        """Delete Encoding Error Webhook"""

        return self.api_client.delete(
            '/notifications/webhooks/encoding/encodings/error/{webhook_id}',
            path_params={'webhook_id': webhook_id},
            type=BitmovinResponse,
            **kwargs
        )

    def getByEncodingIdAndWebhookId(self, encoding_id, webhook_id, **kwargs):
        """Encoding Error Webhook Details for specific Encoding Resource"""

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/error/{webhook_id}',
            path_params={'encoding_id': encoding_id, 'webhook_id': webhook_id},
            type=Webhook,
            **kwargs
        )

    def getByWebhookId(self, webhook_id, **kwargs):
        """Encoding Error Webhook Details"""

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/error/{webhook_id}',
            path_params={'webhook_id': webhook_id},
            type=Webhook,
            **kwargs
        )

    def list(self, query_params: WebhookListQueryParams = None, **kwargs):
        """List Encoding Error Webhooks"""

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/error',
            query_params=query_params,
            pagination_response=True,
            type=Webhook,
            **kwargs
        )

    def listByEncodingId(self, encoding_id, query_params: WebhookListByEncodingIdQueryParams = None, **kwargs):
        """List Encoding Error Webhooks for specific Encoding Resource"""

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/error',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Webhook,
            **kwargs
        )