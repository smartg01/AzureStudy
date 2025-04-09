# Terraform Providers

* Terraform providers are distributed via Hashicorp via the TF registry (registry.terraform.io).

* There are 3 types of providers:

    * Official providers which are owned and maintained by Hashicorp. They have a gold badge next to the logo.
    * Partner provider which are owned and maintained by 3rd parties but has been reviewed and tested by Hashicorp. Can be identified with a purple badge
    * Communitity providers which are maintained by individual contributors. 

* tf init installs the provider in the .terraform registry. 

## Multiple providers in 1 config file

Within the the provider block, you can specify multiple providers which will be installed in the .terraform directory.

## Provider versions

Unless specified the TF config will always download the latest version of the provider. You will need to specify the version you want in the provider block. You can also specify a range of providers that you want to use, for example

```bash
version = ">1.2.0, <2.0.0, !=1.4.0"
```

">"1.2.0: This part ensures that only versions greater than 1.2.0 are allowed. For example, 1.2.1 or 1.3.0 would satisfy this condition, but 1.2.0 itself would not.

<2.0.0: This restricts the acceptable versions to those less than 2.0.0. This means that versions like 1.9.9 or 1.5.0 are valid, but 2.0.0 or anything higher is excluded.

!=1.4.0: This explicitly excludes version 1.4.0 from the acceptable range. Even though it falls between 1.2.0 and 2.0.0, it is specifically disallowed, likely due to known issues or incompatibilities with that version.


### Pessimistic constraint operator

The ~> operator, often referred to as the pessimistic constraint operator, is used in version constraints to specify a range of acceptable versions while allowing updates that do not break compatibility. It is commonly used in Terraform and other tools to ensure that minor or patch updates are allowed, but major version changes are not.

```bash
version = "~> 1.2.0"
```

The above will only allow version 1.2.0, 1.2.1, 1.2.2 until 1.2.9 (or unless it runs out before).

```bash
version = "~> 1.2"
```

The above will only allow version 1.2, 1.3, 1.4. until 1.9 (or unless it runs out before).

## Aliases

You can use the same provider with different settings by declaring the provider multiple times and assigning an alias to each instance. These aliases can then be referenced in your resource blocks to apply the specific provider settings as needed.