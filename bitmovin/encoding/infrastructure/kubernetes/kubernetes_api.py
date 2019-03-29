# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.kubernetes_cluster import KubernetesCluster
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.infrastructure.kubernetes.status.status_api import StatusApi
from bitmovin.encoding.infrastructure.kubernetes.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.infrastructure.kubernetes.configuration.configuration_api import ConfigurationApi
from bitmovin.encoding.infrastructure.kubernetes.agentDeployment.agent_deployment_api import AgentDeploymentApi
from bitmovin.encoding.infrastructure.kubernetes.prewarmedDeployment.prewarmed_deployment_api import PrewarmedDeploymentApi
from bitmovin.encoding.infrastructure.kubernetes.kubernetes_cluster_list_query_params import KubernetesClusterListQueryParams


class KubernetesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(KubernetesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.status = StatusApi(
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

        self.configuration = ConfigurationApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.agentDeployment = AgentDeploymentApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.prewarmedDeployment = PrewarmedDeploymentApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, kubernetes_cluster, **kwargs):
        """Connect Kubernetes Cluster"""

        return self.api_client.post(
            '/encoding/infrastructure/kubernetes',
            kubernetes_cluster,
            type=KubernetesCluster,
            **kwargs
        )

    def delete(self, infrastructure_id, **kwargs):
        """Disconnect Kubernetes Cluster"""

        return self.api_client.delete(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, infrastructure_id, **kwargs):
        """Kubernetes Cluster Details"""

        return self.api_client.get(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=KubernetesCluster,
            **kwargs
        )

    def list(self, query_params: KubernetesClusterListQueryParams = None, **kwargs):
        """List Kubernetes Cluster"""

        return self.api_client.get(
            '/encoding/infrastructure/kubernetes',
            query_params=query_params,
            pagination_response=True,
            type=KubernetesCluster,
            **kwargs
        )