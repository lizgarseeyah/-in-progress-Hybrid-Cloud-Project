# Part 1: On-Prem to Cloud Migration

The first part will focus on migrating resources to the cloud. Here are a few images of the on-prem location and the servers that will be used:

## On-Premise Server Details:
Location: San Jose, CA

**Server 1: BigTwin 2029BZ-HNR**

![server1](https://github.com/lizgarseeyah/-in-progress-Hybrid-Cloud-Project/blob/master/img/server1.png)

Node A:

- OS: Ubuntu 18.04
- CPU: 2 x Intel(r) Xeon(r) Platinum 8276M CPU @ 2.20GHz
- Memory: 24xDIMMs (MEM-DR432L-CL01-ER29 - 16GB RDIMM 2933)
- Storage: 1 x SSDPE2KE032T8

Node B:

- OS: Ubuntu 18.04
- CPU: 2 x Intel(r) Xeon(r) Platinum 8276L CPU @ 2.20GHz
- Memory: 16xDIMMs (MEM-DR416L-CL01-ER29 - 16GB RDIMM 2933)
- Storage: 1 x SSDPE2KE032T8

Node C:

- OS: Red Hat 7.6
- CPU: 2 x CLX (24 cores) -> P4X-SMPMPQRC2-001 QS SMP QRC2/B0 CLX-SRV 8260L 24C 2.4G 35.75M FC-LGA14B 165W
- Memory: 12xDIMMs (MEM-DR432L-CL01-ER29 - 16GB RDIMM 2933)
- Storage: 1 x SSDPE2KE032T8

Node D:

- OS: Red Hat 7.6
- CPU: 2 x Intel(r) Xeon(r) Gold 5215L CPU @ 2.50GHz
- Memory: 12xDIMMs (MEM-DR416L-CL01-ER29 - 16GB RDIMM 2933)
- Storage: 1 x SSDPE2KE032T8

_All node BMCs connected to SSE-X3348T 10G Ethernet Switch_

![switch](https://github.com/lizgarseeyah/-in-progress-Hybrid-Cloud-Project/blob/master/img/switch.png)

**Server 2: Ultra 1029U-10NRT**

![server2](https://github.com/lizgarseeyah/-in-progress-Hybrid-Cloud-Project/blob/master/img/server2.jpg)

- OS: Ubuntu 18.04
- CPU: 2 x Intel(r) Xeon(r) Platinum 8276 CPU @ 2.20GHz
- Memory: 12 x Mem-DR432L-CL01-ER29
- Storage: HDD Seagate Exos 7E2000 1 TB

_BMC/PXE Connected to SSE-G3648B 1G Ethernet Switch_


```markdown
 `Code` text
```

## Step 1: Prepare a Migration Plan
on-prem Requirements: Software:

Ubuntu/RedHat
MySQL Server
Architecture Requirements:

Secure connection between on-prem/cloud
Back-up data before migration
VPC + SG, Firewall, Monitoring alerts, NACLs
DB, Storage regular backups in S3
2 groups in IAM
allow remote connections
create a snapshot, or config template of resources
Multi-AZ, load balanced, scalable
Prevent DDOS attacks

## Step 2: Migrate

## Step 3: Test

Scratch Notes

on-prem Requirements: Software:





