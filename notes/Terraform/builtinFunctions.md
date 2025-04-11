# built in functions


## To Set
In Terraform, you can use the toset function to convert a list into a set. Here's an example:

```terraform
variable "example_list" {
  default = ["item1", "item2", "item3", "item1"] # A list with duplicate values
}

output "example_set" {
  value = toset(var.example_list)
}
```

toset: Converts the input list into a set, removing any duplicate values.

## Length function

The length function in Terraform is used to determine the number of elements in a given list, map, or string.

```terraform
variable "example_list" {
  default = ["item1", "item2", "item3", "item4"]
}

output "list_length" {
  value = length(var.example_list)
}
```

## Terraform console

The terraform console command opens an interactive console where you can evaluate Terraform expressions, test functions, and inspect variables or resources in your configuration. It is particularly useful for debugging and experimenting with Terraform syntax.

```bash
terraform console
```

This is helpful for debugging.
