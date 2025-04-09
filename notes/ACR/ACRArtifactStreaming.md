# ACR Artifact streaming

ACR artifact streaming is a way to pull down images faster for your AKS clusters. This is required for large images over 500MB. Artifact streaming uses a technology called "Accelated Container image" & "overlayBD" when artifact streaming, which breaks down the image into layers and when an ACR pull is in effect, it streams the image layers to the nodepools memory as opposed to the nodepools downloading and unzipping files. 

https://github.com/containerd/accelerated-container-image
https://github.com/containerd/overlaybd
https://github.com/Azure/AKS/issues/3928