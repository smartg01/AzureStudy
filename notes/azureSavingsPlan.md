# Azure Savings plan

* Azure Savings plan is different to reservations because of the following:
    * Azure Reservations is applied to 1 SKU in 1 region making it very rigid. Savings plan can be applied across all locations and SKUs (T&Cs applied)
    * Azure Savings plan is applied across all compute making it more flexible. 

* How does the billing work??
    * Azure runs a billing job every hour to adjust the cost as per the savings plan (Same with reservations). 
    * It applies the discount at the most expensive resource to ensure the biggest discount. 

* Some compute resources it can only be a part of the savings plan if some T&CS are met, such as:
    * Function apps needs to be using a premium SKU
    * App services need to be in isolated tier. 

* Reservations will still be cheaper. Some examples advise that reservations are 10% cheaper for VMs as opposed to a savings plan.

* Licencing is not included. 

* Azure Functions provide a 17% discount on a savings plan over both 1 year term or 3 year term.

* You can transfer your reservations to savings plan.
    * https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/reservation-trade-in