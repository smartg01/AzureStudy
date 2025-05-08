## Storage Account CBAC & RBAC access

Storage account can have claims based access control via the Storage Account access keys. 

If you want it to default to RBAC you need to ensure that "Default to Microsoft Entra authorization in the Azure portal" is enabled. 

Best practice is to disable "Allow storage account key access" to deny CBAC in favour of RBAC. 