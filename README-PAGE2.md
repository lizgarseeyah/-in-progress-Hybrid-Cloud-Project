# Part 1: On-Prem to Cloud Migration

The first part will focus on migrating resources to the cloud. Below are details about the systems used in this part.

## On-Premise Server Details:
Location: San Jose, CA

## **Server 1: BigTwin 2029BZ-HNR**

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

## **Server 2: Ultra 1029U-10NRT**

![server2](https://github.com/lizgarseeyah/-in-progress-Hybrid-Cloud-Project/blob/master/img/server2.jpg)

- OS: Ubuntu 18.04
- CPU: 2 x Intel(r) Xeon(r) Platinum 8276 CPU @ 2.20GHz
- Memory: 12 x Mem-DR432L-CL01-ER29
- Storage: HDD Seagate Exos 7E2000 1 TB

_BMC/PXE Connected to SSE-G3648B 1G Ethernet Switch_


```markdown
 `Code` text
```

## Prepare a Migration Plan

AR: Create migration plan/checklist

- Identify critical pieces and dependencies
- Identify what to migrate first
- create a backup plan
- create a test plan
- create a checklist

_don't forget to_:
- automate scheduled backups
- Setup cloud watch
- Setup up cloud logs
- setup up firewall
- configure SSO
- SSL and encrypt info


## Design the Cloud Architecture

![highlevel-arch](https://github.com/lizgarseeyah/-in-progress-Hybrid-Cloud-Project/blob/master/img/architecture-sketch.jpeg)

The architecture above was designed to meet the following requirements:

**High-Availability and Fault Tolerant:** 

A highly available and fault tolerant architecture is recommended for scenarios or mission critical applications where situations, such as power outages and spikes, would cause the system's performance to dip. The architecture must meet high demand while remaining in operation in case of component failure. Both design attributes go hand in hand. 

Components:
- Multi-AZ Database w/ read replicas and scheduled backups
- Autoscaling Groups
- Load Balancer
- Content Delivery Network (CDN)
- A warm standby or multi-region active site can be added to the second region, to reduce RPO times, but it is a more costly option.

**Cost-Effective Failure and Disaster Recovery (DR) Plan:**

Since we are assuming a non-mission critical scenario, a cost-effective DR plant would be to spin up an new architecture in a different, existing region using the replicated storage located in that region, i.e. the backup and restore method. This repository would contain the AMI snapshots, configuration templates, database backups, and storage backups to recreate our original architecture. 

**Secure**

This architecture was secured using a virtual private cloud (VPC) along with security groups, Network Access Control Lists (NACLs), and a Virtual Private Gateway to restrict incoming and outgoing traffic. Futhermore, setting up users with the appropriate access, employing strong password requirements, and use of multi-factor authentication adds an additional layer of security. Adding a load balancer and firewall protect against DDoS attacks. Additional elements used: SSL/TLS protocol to secure the web app and server-side and client-side encryption to protect data at rest.

The steps taken to create the cloud architecture is defined below:

![cloud-arch-steps](https://github.com/lizgarseeyah/-in-progress-Hybrid-Cloud-Project/blob/master/img/cloud_arch.jpg)

## Migrate

## Test

test scenarios:

- high traffic
- DDoS
- SSO functionality
- Website and python program functionality
- can i access: storage and website?
- Migration process
- Blue-Green process
- log automation (lambda function)



