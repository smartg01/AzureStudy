# Terraform state

* State files have the file name "terraform.tfstate" & they have backups called "terraform.tfstate.backup"

* The state file is in JSON format. 

* State file is the single source of truth as to the state of your infrastructure / items created by Terraform. 

* When running a TF plan, it reviews the state file and analyses what is the actual state of the state vs the declared state in the code.

* Terraform state files can contain sensitive information which is why remote states are better practice.

## Remote State

* Remote state is a option to store TF state files in a shared storage location such as S3 bucket, Azure Storage Account or Terraform Cloud. 
