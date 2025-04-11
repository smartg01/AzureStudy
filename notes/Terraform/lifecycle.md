# lifecycle 

lifecycle input blocks allow you to tell Terraform how you would like the lifecycle of the resource to be managed. 

## Create before destory function

This function allows you to tell Terraform to create a new resource 1st before destroying the existing 1. 

## prevent destory = true

This add a terraform based resource lock for destructive **CHANGES, this does not excempt the resource from Terraform destroy command**

## life cycle example

please see below a life cycle example which would ignore changes to the tags argument values.

```terraform
resource "azurerm_resource_group" "rg" {
    name = "test"
    location = "australieast"

    lifecycle {
        ignore_changes = [
            tags
        ]
    }
}
```