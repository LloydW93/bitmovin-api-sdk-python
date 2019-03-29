# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.email_notification import EmailNotification
from bitmovin.models.encoding_error_email_notification import EncodingErrorEmailNotification
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError


class ErrorApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ErrorApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_error_email_notification, **kwargs):
        """Add Encoding Error Email Notification (All Encodings)"""

        return self.api_client.post(
            '/notifications/emails/encoding/encodings/error',
            encoding_error_email_notification,
            pagination_response=True,
            type=EncodingErrorEmailNotification,
            **kwargs
        )

    def createByEncodingId(self, encoding_id, email_notification, **kwargs):
        """Add Encoding Error Email Notification (Specific Encoding)"""

        return self.api_client.post(
            '/notifications/emails/encoding/encodings/{encoding_id}/error',
            email_notification,
            path_params={'encoding_id': encoding_id},
            type=EmailNotification,
            **kwargs
        )

    def update(self, notification_id, email_notification, **kwargs):
        """Replace Encoding Error Email Notification"""

        return self.api_client.put(
            '/notifications/emails/encoding/encodings/error/{notification_id}',
            email_notification,
            path_params={'notification_id': notification_id},
            type=EmailNotification,
            **kwargs
        )
