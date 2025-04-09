# HCL basics

* HCL stands for Hashicorp config language (file type of .tf) which are made of blocks and arguments. 
    * Blocks provide info about infrastructure we want to create.
    * Block types are declared at the beginning of the resource IE "resource" OR "Data".
    * After the block type has been established, the resource type is specified. This is specified via "Provider"_"Resource". For example, Azurerm_Resource_Group.
    * Resource name then follows the resource type. This is a logical name for the block.

* Within the blocks we have the arguments for the block which specifies certain items for the resource we want to create.





**Block type****Resource Type****Logical resource name**
    |               |               |
    |               |               |
    |               |               |
    v               v               v
````
resource "azurerm_resource_group" "RG" {              |       
    name     = "test"                                 |       
    location = "australia easy"                       |     
}
```

* Resource is a thing which Terraform will manage, such as VMs or AKS. 