## Conditions

Terraform conditions allow you to use conditional logic to dynamically set values based on certain criteria. This is achieved using the ternary operator (`condition ? true_value : false_value`).

### Example: Conditional Resource Tagging

```terraform
variable "environment" {
  default = "production"
}

resource "azurerm_resource_group" "example" {
  name     = "example-rg"
  location = "East US"

  tags = {
    environment = var.environment
    cost_center = var.environment == "production" ? "1001" : "1002"
  }
}

```
### Explanation
Condition: var.environment == "production"
True Value: "1001"
False Value: "1002"
If the environment variable is "production", the cost_center tag will be set to "1001". Otherwise, it will be set to "1002".