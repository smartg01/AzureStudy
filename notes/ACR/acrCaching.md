# ACR caching

This document details what Azure Container Registry is and what is it used for. 

## What is ACR caching

ACR caching is a feature for ACRs which allows ACRs to cache public repo container images. This is completed via Cache ACR rules where you need to specify the public repo and the image in question. Please note that it wont automatically pull down the latest image from the public ACR, but if a new version which is not in the ACR, it will be pulled and then re-cached.


## Benefits of ACR Caching

The benefits of ACR caching are as followed:

* Faster and more reliable image pulls. This is being pulled over an ACR via the MSFT backbone which will be much faster & if the image is cached then there is no reliance on 3rd party. (& provide better performance effiency & reliability).

* Ensuring upstream content is delivered — All registries, especially public ones like Docker Hub and others, have limits on the number of anonymous pulls. This is to make sure that they can serve everyone. With ACR caching, users can get images from the local ACR instead of the upstream registry.