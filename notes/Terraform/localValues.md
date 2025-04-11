# Local values

Terraform **local values** are named expressions that simplify and reduce repetition in your configuration. They allow you to assign a value to a name, which can then be reused throughout your configuration. This makes your code cleaner, easier to read, and maintainable.

### Example: Azure Tags

```terraform
locals {
  common_tags = {
    environment = "production"
    owner       = "team-azure"
    project     = "example-project"
  }
}

resource "azurerm_resource_group" "example" {
  name     = "example-rg"
  location = "East US"

  tags = local.common_tags
}