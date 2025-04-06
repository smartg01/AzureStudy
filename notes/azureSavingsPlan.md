# Azure Savings plan

Azure savings plans help you save money by committing to an hourly spend for one-year or three-year plans for Azure compute resources. **SAVINGS UPTO 65%**

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

* Licencing is not included in the savings plan so you will pay the full amount for windows & SQL licencing. 

* Azure Functions provide a 17% discount on a savings plan over both 1 year term or 3 year term.

* You can transfer your reservations to savings plan.
    * https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/reservation-trade-in

* Azure recommendations highlights what savings can be made with a savings plan. Please note that the recommendations do a 30 day look back so anything before the 30 days (like something that was temp deployed for a SBX test 60 days ago) will not be picked up in the recommendation scan.

* Once a savings plan is purchased, you can make the following changes to a savings plan:
    * Update a savings plan scope.
    * Change autorenewal settings.
    * View savings plan details and utilization.
    * Delegate savings plan role-based access control (RBAC) roles.