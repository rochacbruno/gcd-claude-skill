# Configure firewall rules

Source: https://documentation.s3ns.fr/filestore/docs/configuring-firewall
Last updated: 2026-10-26

Some or all of the information on this page might not apply to Cloud de Confiance by S3NS. See [Differences from Google Cloud](/filestore/docs/tpc-differences) for more details.














- 





[

Home

](https://documentation.s3ns.fr/)






- 








[

Documentation

](https://documentation.s3ns.fr/docs)






- 








[

Storage

](https://documentation.s3ns.fr/docs/storage)






- 








[

Filestore

](https://documentation.s3ns.fr/filestore/docs)






- 








[

Guides

](https://documentation.s3ns.fr/filestore/docs/overview)












# Configure firewall rules 














This page explains when you must configure firewall rules to enable NFS file
locking.

## Conditions that require firewall ingress rule configuration

You must create a firewall ingress rule to enable traffic from
Filestore instances to your clients if:

- You are using NFS file locking in the applications accessing the
Filestore instance.

- 

The VPC network you are using has firewall rules that block TCP port 111
or the ports used by the `statd` or `nlockmgr` daemons. To determine what
ports the `statd` and `nlockmgr` daemons use on the client,
[check current port settings](/filestore/docs/setting-nfs-ports#checking-ports).

If the `statd` and `nlockmgr` ports aren't set, and you think you might need
to configure firewall rules at any point, we strongly recommend setting those
ports consistently on all client VM instances. For more information, see
[Setting NFS ports](/filestore/docs/setting-nfs-ports).

## Conditions that require firewall egress rule configuration

You must create a firewall egress rule to enable traffic from your clients to
your Filestore instances if:

- The VPC network you're using has a firewall egress rule for the
IP address ranges used by your Filestore instances.

- The firewall egress rule blocks traffic to TCP ports 111, 2046, 2049, 2050, or
4045.

You can get the reserved IP address range for any Filestore
instance from
[the Filestore instances page](https://console.cloud.s3nscloud.fr/filestore/instances)
or by running `gcloud filestore instances describe`. For more information, see
[Get information about a specific instance](/filestore/docs/getting-instance-information#get-instance).

For more information about VPC network firewall rules, see
[Using Firewall Rules](/vpc/docs/using-firewalls).

## Create a firewall ingress rule

Use the following procedure to create a firewall rule to enable traffic from
Filestore instances.

- 

Before you begin, verify the following:



### Windows

- 

Confirm that the client is allowed to communicate with the Filestore
instance and that the local firewall is not blocking the required ports.
To open all required NFS ports, run the following command in PowerShell:


```
'111' , '2046' , '2049' , '2050' , '4045' | % { 
C: \W indows \s ystem32 \n etsh.exe advfirewall firewall add rule name = "NFS Shares allow TCP/UDP port $( $_ ) " dir = IN action = ALLOW protocol = TCP,UDP localport = $( $_ ) 
} 
```


- 

[Check current port settings](/filestore/docs/setting-nfs-ports#current-ports)
to determine what ports the `statd` and `nlockmgr` daemons use on the
client. Make note of them for later use.



### Linux

No prerequisites for completing this task.


### MacOS

No prerequisites for completing this task.



- 

Go to the **Firewall** page in the Cloud de Confiance console. 

[Go to the Firewall page](https://console.cloud.s3nscloud.fr/networking/firewalls/list) 

- 

Click **Create firewall rule**.

- 

Enter a **Name** for the firewall rule.
This name must be unique for the project.

- 

Specify the **Network** in which you want to implement the firewall rule.

- 

Specify the **Priority** of the rule.

If this rule doesn't conflict with any other rules, you can leave the default
of `1000`. If an existing ingress rule has **Action on match: Deny** set for
the same IP address range, protocols, and ports, then set a lower priority
than the existing ingress rule.

- 

Choose **Ingress** for **Direction of traffic**.

- 

Choose **Allow** for **Action on match**.

- 

For **Targets**, take one of the following actions:

- If you want to allow traffic to all clients in the network from
Filestore instances, choose **All instances in the network**.

- If you want to allow traffic to specific clients from
Filestore instances, choose **Specified target tags**. Type
the instance names of the clients in **Target tags**.

- 

Leave the default value of **IP ranges** for **Source filter**.

- 

For **Source IP ranges**, enter the IP address ranges of the Filestore
instances you want to allow access from in CIDR notation. You can enter the
[internal IP address ranges](https://www.arin.net/knowledge/address_filters.html)
that you are using with your Filestore instances to enable all
Filestore traffic. You can also enter the IP addresses of
specific Filestore instances.

- 

Leave the default value of **None** for **Second source filter**.

- 

For **Protocols and ports**, choose **Specified protocols and ports** and
then:

- Select the **tcp** checkbox and enter
`111, STATDOPTS , nlm_tcpport `
in the associated field, where:

- STATDOPTS is the port used by the `statd` daemon on the
client.

- nlm_tcpport is the `tcp` port used by the `nlockmgr` daemon
on the client.

- Select the **udp** checkbox and enter the value of `nlm_udpport`, which
is the `udp` port used by `nlockmgr`. Note that these specifications
apply to the following [service tiers](/filestore/docs/service-tiers)
only:

- Zonal

- Regional

- Enterprise

- 

Choose **Create**.

## Create a firewall egress rule

Use the following procedure to create a firewall rule to
enable traffic to Filestore instances.

- 

Before you begin, verify the following:



### Windows

Confirm that the client is allowed to communicate with the Filestore
instance and that the local firewall is not blocking the required ports.
To open all required NFS ports, run the following command in PowerShell:


```
'111' , '2046' , '2049' , '2050' , '4045' | % { 
C: \W indows \s ystem32 \n etsh.exe advfirewall firewall add rule name = "NFS Shares allow TCP/UDP port $( $_ ) " dir = OUT action = ALLOW protocol = TCP,UDP localport = $( $_ ) 
} 
```


### Linux

No prerequisites for completing this task.


### MacOS

No prerequisites for completing this task.



- 

Go to the **Firewall** page in the Cloud de Confiance console. 

[Go to the Firewall page](https://console.cloud.s3nscloud.fr/networking/firewalls/list) 

- 

Click **Create firewall rule**.

- 

Enter a **Name** for the firewall rule.
This name must be unique for the project.

- 

Specify the **Network** in which you want to implement the firewall rule.

- 

Specify the **Priority** of the rule.

If this rule doesn't conflict with any other rules, you can leave the default
of `1000`. If an existing egress rule has **Action on match: Deny** set for
the same IP address range, protocols, and ports, then set a lower priority
than the existing ingress rule.

- 

Choose **Egress** for **Direction of traffic**.

- 

Choose **Allow** for **Action on match**.

- 

For **Targets**, take one of the following actions:

- If you want to allow traffic from all clients in the network to
Filestore instances, choose **All instances in the network**.

- If you want to allow traffic from specific clients to
Filestore instances, choose **Specified target tags**. Type
the instance names of the clients in **Target tags**.

- 

For **Destination IP ranges**, enter the IP address ranges of the Filestore
instances you want to allow access to in CIDR notation. You can enter the
[internal IP address ranges](https://www.arin.net/knowledge/address_filters.html)
that you are using with your Filestore instances to enable
traffic to all Filestore instances. You can also enter the IP
addresses of specific Filestore instances.

- 

For **Protocols and ports**, choose **Specified protocols and ports**. Then
select the **tcp** checkbox and enter `111,2046,2049,2050,4045` in the
associated field.

- 

Choose **Create**.

## Verify NFS ports

We recommend verifying whether your NFS ports have been opened properly. For
more information, see [Configure NFS ports on client VMs](/filestore/docs/setting-nfs-ports#verify-ports).

## What's next

- [Learn more about the networking and IP resource requirements for using
Filestore](/filestore/docs/networking).

- [Configure NFS ports on client VMs](/filestore/docs/setting-nfs-ports).