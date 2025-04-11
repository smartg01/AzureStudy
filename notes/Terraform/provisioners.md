# Provisioners in Terraform

Provisioners in Terraform are used to execute scripts or commands on a local or remote machine as part of the resource lifecycle. They are typically used for tasks like bootstrapping a server, configuring software, or running custom scripts after a resource is created or destroyed. However, provisioners should be used sparingly, as they can introduce complexity and dependencies that Terraform is not designed to manage.

* Types of Provisioners
    * local-exec: Executes a command on the machine running Terraform.
    * remote-exec: Executes a command on a remote resource, such as a virtual machine.


``` Terraform
resource "azurerm_virtual_machine" "example" {
  name                  = "example-vm"
  location              = azurerm_resource_group.example.location
  resource_group_name   = azurerm_resource_group.example.name
  network_interface_ids = [azurerm_network_interface.example.id]
  vm_size               = "Standard_DS1_v2"

  os_profile {
    computer_name  = "examplevm"
    admin_username = "adminuser"
    admin_password = "P@ssw0rd1234!"
  }

  os_profile_linux_config {
    disable_password_authentication = false
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y nginx"
    ]

    connection {
      type     = "ssh"
      user     = "adminuser"
      password = "P@ssw0rd1234!"
      host     = self.public_ip_address
    }
  }
}
```

## Local exec provisioner

```terraform
resource "null_resource" "example" {
  provisioner "local-exec" {
    command = "echo 'Hello, Terraform!' > output.txt"
  }
}
```

