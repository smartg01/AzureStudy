# Resource Targeting in Terraform

Resource targeting in Terraform allows you to apply or destroy specific resources within your configuration without affecting the rest of the infrastructure. This is particularly useful for testing, debugging, or making incremental changes.

## How to Target Resources

### Apply Specific Resources
To apply changes to a specific resource, use the `-target` flag with the `terraform apply` command:

```bash
terraform apply -target=resource_type.resource_name