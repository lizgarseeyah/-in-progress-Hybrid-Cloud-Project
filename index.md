# (in-progress) Hybrid Cloud Project

This project has multiple goals: gain experience migrating from on-premise to the cloud and deploy a web application in a blue green deployment scenario. This process will use full-stack development to explore how to leverage cloud technologies in different ways while integrating best practices at each stage. This project has been divided into three parts:

**Part 1: Migrate and Rehost Resources**

For the first part of this project, I will be migrating an architecture on a _[Supermicro Server]_and rehost the services in the AWS environment.

**Part 2: Web Application Development**

This second part will focus on the front-end development of the application. _tbd_

**Part 3: Deploy the Web Application in a Blue-Green Envrionment**

The third part of this project is to test the web app and the network, security, and functionality of the cloud architecture. The web app will be deployed in a blue environment first, where the application, and architecture security, and operation will be tested. Once that is completed, the final step in this project is to deploy the application in the green environment and ensure the architecture and web app meet the requirements.

## On-Premise Server Details:
Location: San Jose, CA

Server 1:

BigTwin 2029BZ-HNR

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

* All node BMCs connected to SSE-X3348T 10G Ethernet Switch

![Image](src)
Server 2:

Ultra 1029U-10NRT

- OS: Ubuntu 18.04
- CPU: 2 x Intel(r) Xeon(r) Platinum 8276 CPU @ 2.20GHz
- Memory: 12 x Mem-DR432L-CL01-ER29
- Storage: HDD Seagate Exos 7E2000 1 TB

* BMC/PXE Connected to SSE-G3648B 1G Ethernet Switch

![Image](src)

```markdown
 `Code` text
```
![Image](/Hybrid-Cloud-Project/img/architecture-sketch.jpeg)
