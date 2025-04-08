# AKS Isolated Networking

Azure Kubernetes Service has a Isolated networking option which requires no egress traffic beyond the VNet. During the bootstrapping cluster process, AKS would need to reach out to the public internet to get packages from the MAR (Microsoft Artifact Registry). This adds extra overhead to cost (due to cost of FW), operational excellence (Reducing the need for a FW reduces chances of potential issues) & performance efficiency (AKS will be faster as it doesnt need to reach out to internet or traverse to different resources, it can pull all the artifatcs it needs from its local ACR.). This will also reduce complexity to security with no egress required. 

* ![Reference architecture from MSFT](images\image.png)

* 2 options regarding ACRs
    * Fully managed ACR by AKS. Cluster will manage the ACR itself with no intevnetion required from support. 
    * BYO ACR. This requires an ACR Private Endpoint.

* If the images aren't present, the private ACR pulls them from MAR and serves them via its private endpoint, eliminating the need to enable egress from the cluster to the public MAR endpoint. This is completed via the Azure backbone!