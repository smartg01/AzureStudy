 Dynamic Blocks and Splat Expressions

## Dynamic Blocks

Dynamic blocks in Terraform allow you to generate nested blocks dynamically based on a variable or other input. This is useful when the number of nested blocks is not fixed and depends on input data.

### Example: Dynamic Blocks for Azure NSG Rules

```terraform
variable "nsg_rules" {
  default = [
    { name = "rule1", priority = 100, direction = "Inbound" },
    { name = "rule2", priority = 200, direction = "Outbound" }
  ]
}

resource "azurerm_network_security_group" "example" {
  name                = "example-nsg"
  location            = "East US"
  resource_group_name = "example-rg"

  dynamic "security_rule" {
    for_each = var.nsg_rules
    content {
      name                       = security_rule.value.name
      priority                   = security_rule.value.priority
      direction                  = security_rule.value.direction
      access                     = "Allow"
      protocol                   = "*"
      source_port_range          = "*"
      destination_port_range     = "*"
      source_address_prefix      = "*"
      destination_address_prefix = "*"
    }
  }
}
```



* Explanation:
    * dynamic Block: Generates security_rule blocks dynamically for each item in var.nsg_rules.
    * for_each: Iterates over the list of rules defined in the variable.
    * content: Defines the structure of each dynamically generated block.



# Splat Expressions in Terraform

Splat expressions in Terraform are used to extract values from a list of resources or attributes. They simplify accessing multiple values at once, making configurations more concise and readable.

## Example: Splat Expression for Resource Outputs

```terraform
resource "azurerm_virtual_machine" "example" {
  count    = 3
  name     = "example-vm-${count.index}"
  location = "East US"
}

output "vm_names" {
  value = azurerm_virtual_machine.example[*].name
}
```
[*]: The splat operator extracts the name attribute from all instances of the azurerm_virtual_machine resource.
Output: The vm_names output will be a list of all VM names, e.g., ["example-vm-0", "example-vm-1", "example-vm-2"].