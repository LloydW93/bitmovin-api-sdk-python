# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except
from bitmovin.notifications.webhooks.encoding.encoding_api import EncodingApi


class WebhooksApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(WebhooksApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.encoding = EncodingApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
