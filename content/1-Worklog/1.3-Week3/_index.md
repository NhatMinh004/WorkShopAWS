---
title: "Week 3 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---
{{% notice warning %}} 
⚠️ **Note:** The following information is for reference purposes only. Please **do not copy verbatim** for your own report, including this warning.
{{% /notice %}}


### Week 3 Objectives:

* Complete VPC networking deployment, configure internet routing via NAT Gateway & IGW, and set up Security Groups.
* Launch EC2 instances in subnets and configure secure connection methods using EC2 Instance Connect Endpoint.
* Learn and implement Hybrid DNS resolution across Cloud and On-premises environments via Route 53 Resolver.
* Connect to RDP via RDGW, test DNS resolution results, and perform lab resource cleanup.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **Configure VPC Routing & Security:** <br>&emsp; + Module 02-Lab03-03.3 - Create an Internet Gateway <br>&emsp; + Module 02-Lab03-03.4 - Create Route Table for Outbound Internet Routing via Internet Gateway <br>&emsp; + Module 02-Lab03-03.5 - Create security groups | 04/05/2026 | 04/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Launch Instances & Configure NAT Routing:** <br>&emsp; + Module 02-Lab03-04.1 - Create EC2 Instances in Subnets <br>&emsp; + Module 02-Lab03-04.2 - Test connection <br>&emsp; + Module 02-Lab03-04.3 - Create NAT Gateway <br>&emsp; + Module 02-Lab03-04.5 - EC2 Instance Connect Endpoint | 05/05/2026 | 05/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Initialize Hybrid DNS Infrastructure:** <br>&emsp; + Module 02-Lab10-01 - Set up Hybrid DNS with Route 53 Resolver (Introduction) <br>&emsp; + Module 02-Lab10-02.1 - Generate Key Pair <br>&emsp; + Module 02-Lab10-02.2 - Initialize CloudFormation Template <br>&emsp; + Module 02-Lab10-02.3 - Configure Security Group | 06/05/2026 | 06/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **Configure RDGW & DNS Outbound Endpoint:** <br>&emsp; + Module 02-Lab10-03 - Connect to RDGW <br>&emsp; + Module 02-Lab10-05 - Set up DNS <br>&emsp; + Module 02-Lab10-05.1 - Create Route 53 Outbound Endpoint | 07/05/2026 | 07/05/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Configure Resolver Rules, Inbound Endpoints & Clean up:** <br>&emsp; + Module 02-Lab10-05.2 - Create Route 53 Resolver Rules <br>&emsp; + Module 02-Lab10-05.3 - Create Route 53 Inbound Endpoints <br>&emsp; + Module 02-Lab10-05.4 - Test results <br>&emsp; + Module 02-Lab10-06 - Clean up resources | 08/05/2026 | 08/05/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Week 3 Achievements:

* Deployed a fully functional VPC routing configuration allowing public subnets to access the Internet via IGW and private subnets via NAT Gateway.
* Launched EC2 instances successfully inside multiple VPC subnets.
* Configured and used EC2 Instance Connect Endpoint to establish secure SSH/RDP sessions without requiring public IPs or Bastion Hosts.
* Used AWS CloudFormation to automatically provision infrastructure for the Hybrid DNS lab environment.
* Created a Hybrid DNS solution capable of resolving domain names between On-Premises and AWS Cloud via Route 53 Resolver Inbound/Outbound Endpoints & Rules.
* Established Remote Desktop Gateway (RDGW) connection successfully.
* Cleaned up all resources to keep billing at a minimum.
