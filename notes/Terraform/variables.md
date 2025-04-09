# Variables

* Variables can be declared as opposed to be hard coded. 
* Default values can be overridden. 
* Variables with no values can have values assigned to them when running TF apply via the interactive mode in the terminal.
* You can also use environment variables to declare values. Such as:

```
export TF_VAR_rg_name="RGName"
Terraform apply
```

Please note that TF_VAR must be in all caps.

* You can also pass values through via a file like this

```
terraform apply -var-file=test.auto.tfvars
```

* You can also pass random values in the apply stage.

```
terraform apply -var="environment=test"
```

* Please note that any file in the directorywith the following file type is automatically loaded.
    * terraform.tfvars
    * *.auto.tfvars
    * terraform.tfvars.json
    * *auto.tfvars.json

### Terraform order of acceptance for variables

Variable defintion presidence

|Load Order|Option| Priority |
|----|-------|-------|
|1|Environment variable| 4 |
|2|terraform.tfvars| 3 |
|3|*.auto.tfvars (alphabetical order)| 2 |
|4| -var OR -var-file flags in command line| 1 |

-var flags are the highest priority, followed by *auto.tfvars.

### Validation rules 

Within variable blocks, we can define a validation block which specifies what HCL is expecting when values are passed to the variable. If the condition is not met, you can pass an error message which will load into the terminal when running TF. 

### Variable types

### Variable types

| Type     | Example                                      | Definition                                                                 |
|----------|----------------------------------------------|---------------------------------------------------------------------------|
| String   | "This is a string"                          | A sequence of characters, typically used for text values.                 |
| Int      | 1                                            | A whole number, used for numeric values without decimals.                 |
| Boolean  | true                                         | A true or false value, used for binary conditions.                        |
| List     | ["item1", "item2", "item3"]                 | An ordered collection of values of the same type.                         |
| Set     | ["item1", "item2", "item3"]                 | Same as a list but cannot have duplicate values.                         |
| Map      | { key1 = "value1", key2 = "value2" }        | A collection of key-value pairs, where keys are unique strings.           |
| Object   | { name = "example", age = 30, active = true }| A complex type with named attributes, each having its own type.           |
| Tuple    | ["string", 1, true]                         | An ordered collection of values of different variable types.                       |


If you do not specify a type, Terraform will select `any` and match it to the value that is passed.



