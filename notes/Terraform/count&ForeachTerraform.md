## Count and For-each

* These are meta arguments!

* Count is good for looping over lists. Starts with 0 and then goes up by 1 each time. 
* Problem with count is that if you remove something from the list, it then impacts the whole list. 

* For_each does not use list but uses maps or sets. For each is much better when deploying multiple resources. 

### Count and list Example below

```terraform
resource "azurerm_resource_group" "rg" {
    count = length(var.rg_name)
    name = var.rg_name[count.index]
    location = "australiaeast"
}

variable rg_name {
    type = list(string)
}

rg_names = [
    "name1",
    "name2"
]

```

When this is run via Terraform, the resources will be counted like azurerm_resource_group.rg[0] & azurerm_resource_group.rg[1] 

### For_each and map/set Example below

```terraform
resource "azurerm_resource_group" "rg" {
    for_each = var.rg_names
    name     = each.key
    location = each.value
}

variable "rg_names" {
    type = map(string)
}

rg_names = {
    "name1" = "australiaeast"
    "name2" = "australiasoutheast"
}
```
When this is run via Terraform, the resources will be created with unique keys, such as azurerm_resource_group.rg["name1"] and azurerm_resource_group.rg["name2"]. Unlike count, for_each ensures that changes to the map (e.g., adding or removing entries) do not affect unrelated resources. This makes for_each more suitable for managing resources with unique identifiers.