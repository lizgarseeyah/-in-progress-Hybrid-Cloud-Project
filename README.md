# (in-progress) Hybrid Cloud Project

This project has multiple goals: gain experience migrating from on-premise to the cloud and deploy a web application in a blue green deployment scenario. This process will use full-stack development to explore how to leverage cloud technologies in different ways while integrating best practices at each stage. This project has been divided into three parts:

**Part 1: Migrate and Rehost Resources**

For the first part of this project, I will be migrating an architecture on a _[Supermicro Server]_and rehost the services in the AWS environment.

[Part 1 Details](/-in-progress-Hybrid-Cloud-Project/page2.md)

**Part 2: Web Application Development**

This second part will focus on the front-end development of the application. _tbd_

[Part 2 Details](/-in-progress-Hybrid-Cloud-Project/page3.md)

**Part 3: Deploy the Web Application in a Blue-Green Envrionment**

The third part of this project is to test the web app and the network, security, and functionality of the cloud architecture. The web app will be deployed in a blue environment first, where the application, and architecture security, and operation will be tested. Once that is completed, the final step in this project is to deploy the application in the green environment and ensure the architecture and web app meet the requirements.

[Part 3 Details](/-in-progress-Hybrid-Cloud-Project/page4.md)


![Image](/Hybrid-Cloud-Project/img/architecture-sketch.jpeg)


### **_Scratch Notes_**
on-prem Requirements:
Software:
  - Ubuntu/RedHat
  - MySQL Server

Architecture Requirements:
- Secure connection between on-prem/cloud
- Back-up data before migration
- VPC + SG, Firewall, Monitoring alerts, NACLs
- DB, Storage regular backups in S3
- 2 groups in IAM
- allow remote connections
- create a snapshot, or config template of resources
- Multi-AZ, load balanced, scalable
- Prevent DDOS attacks

Applicatin Requirements:
- Web app -> UI/UX Data Science-based project
- Frameworks: React, Node?
- Require SSO login
- Require 2MFA
- SEO optimized
