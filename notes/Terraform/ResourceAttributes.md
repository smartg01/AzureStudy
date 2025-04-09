## Terraform resource attributes    

Terraform resources has several attributes depending on the resource itself. These attributes are exported as standard. These can be used in other resource blocks and there arguments. 

For example:

```terraform
resource "azurerm_resource_group" "rg" {
    name = ""
    location = ""
}

resource "azurerm_storage_account" "sa" {
    name           = ""
    location       = azurerm_resource_group.rg.location
    resource_group = azurerm_resource_group.rg.name ### This is a implicent dependency 
}

```
## implicit dependency

An implicit dependency in Terraform occurs when one resource automatically depends on another due to the use of its attributes or outputs. Terraform recognizes this dependency without requiring explicit configuration, ensuring that the dependent resource is created or updated only after the resource it relies on is ready.


## explicit dependency

An explicit dependency is when you manually define the dependency between resources using the depends_on argument. This is useful when Terraform cannot automatically infer the dependency based on attribute references, or when you want to enforce a specific order of resource creation.

```
resource "azurerm_storage_account" "sa" {
    name           = "examplestorage"
    location       = "East US"
    resource_group = azurerm_resource_group.rg.name

    depends_on = [azurerm_resource_group.rg] # Explicit dependency
}

```

