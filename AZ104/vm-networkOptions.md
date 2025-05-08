# Virtual machine Networking options

* You must have a VNet in the same region & subscription as the machine. Different RG is ok.

# Acclerated networking

Accelated networking stops traffic going through the virtual switch and straight to the network card.

 ![Reference architecture from MSFT](../images/accelerated-networking.png)

 With Accelerated Networking, network traffic that arrives at the VM's network interface (NIC) is forwarded directly to the VM. Accelerated Networking offloads all network policies that the virtual switch applied, and it applies them in hardware. Because hardware applies policies, the NIC can forward network traffic directly to the VM. The NIC bypasses the host and the virtual switch, while it maintains all the policies that it applied in the host.

Best suited for Vm to Vm traffic in the same Vnet.

