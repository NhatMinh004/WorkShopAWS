---
title: "Proposal"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---
{{% notice warning %}}
⚠️ **Note:** The information below is for reference purposes only. Please **do not copy verbatim** for your report, including this warning.
{{% /notice %}}

In this section, you need to summarize the contents of the workshop that you **plan** to conduct.# NodeJ2Car Auto Parts E-Commerce Platform  
## An Optimized AWS Cloud Solution for Performance, Security, and Scalability  

### 1. Executive Summary  
The **NodeJ2Car** project builds a specialized e-commerce system offering premium auto parts. The platform stands out with three breakthrough features: an interactive 2D visual car schematics explorer, real-time client support via WebSockets, and AI-powered diagnostic image scanning to identify broken parts. To meet the requirements of high-concurrency online transactions, strict user data protection, and reliable asynchronous payment processing (VNPay, MoMo, Stripe), the entire system is deployed on AWS utilizing a hybrid container-serverless architecture. This solution enables NodeJ2Car to achieve high availability, elastic scaling, and minimal operational overhead.

### 2. Problem Statement  
*Current Issues*  
1.  **Complex Parts Catalog Navigation:** Auto parts comprise millions of unique part numbers. Average users face significant friction and errors trying to search for matching parts for their specific car models using traditional keyword search.
2.  **System Instability under Real-Time Workloads:** Handling concurrent Socket.io chat connections and external payment callback webhooks (IPN) directly on the main API server can lead to severe bottlenecks, API timeouts, or transaction loss.
3.  **Security Vulnerabilities:** As a financial transaction hub, an e-commerce platform is a high-value target for SQL injections, data breaches, and DDoS attacks.

*The Solution*  
The system addresses these pain points by integrating modern software design with robust AWS cloud services:
*   **Visual 2D Schematics & AI Scan:** Streamlines the parts identification flow, removing the need for customers to memorize complicated part numbers.
*   **Asynchronous Payment Processing:** Decoupled architecture using **AWS Lambda** serverless ingestion and **Amazon SQS** queues, securing transactional logs even if backend API containers fail.
*   **Decentralized WebSockets state:** Utilizes **Amazon ElastiCache Redis** as a pub/sub adapter to synchronize real-time Socket.io messages across all compute tasks.
*   **Comprehensive Edge Shielding:** Hides the compute resources in VPC private subnets behind an **Application Load Balancer (ALB)**, front-ended by **AWS WAF** rules and **Amazon CloudFront CDN**.

*Benefits and Return on Investment (ROI)*  
*   **Boosted Conversion Rates:** Reduces user search time by 70%, translating to lower cart abandonment and higher sales.
*   **99.99% Service Availability:** Multi-AZ container deployments via ECS Fargate ensure seamless failover.
*   **Cost Efficiency:** Eliminates idle server waste through a pay-as-you-go serverless billing model. The break-even period is expected within 6 months due to reduced infrastructure maintenance costs and zero payment loss incidents.

### 3. Solution Architecture  
The platform uses **Amazon VPC** as its security foundation, separating resources into Public and Private subnets across two independent Availability Zones (AZs). External traffic is inspected at the edge by **AWS WAF** and cached globally by **Amazon CloudFront** before reaching the load balancer.

*AWS Services Used*  
- **Amazon VPC:** Networking layout (Public/Private Subnets, NAT Gateways).
- **Amazon ECS & AWS Fargate:** Elastic containerized compute hosting for Node.js backend.
- **Application Load Balancer (ALB):** Traffic load distribution with Sticky Sessions enabled for stable Socket connections.
- **Amazon DocumentDB:** MongoDB-compatible primary-replica database engine.
- **Amazon ElastiCache Redis:** Session cache and Socket.io pub/sub synchronization node.
- **AWS Lambda & Amazon SQS:** Serverless IPN webhook processors and transaction queues.
- **Amazon S3 & S3 Gateway Endpoint:** Hosts React SPA assets and stores product media, utilizing private endpoints to avoid NAT Gateway charges.
- **Amazon CloudFront & AWS WAF:** Global CDN and Web Application Firewall rulesets.
- **Amazon ECR:** Private container registry for Docker images.

*Component Design*  
- **Frontend Tier:** React SPA static bundle hosted on S3 and distributed via CloudFront.
- **Backend Tier:** Express API tasks in private subnets, routed via ALB.
- **Integration Tier:** Webhooks trigger serverless Lambda functions, which queue transaction messages in SQS for backend workers to consume.
- **Data Tier:** DocumentDB cluster running a primary write node in AZ1 and a replica read node in AZ2.

### 4. Technical Implementation  
*Implementation Phases*  
The project is divided into four main execution phases:
1.  **Phase 1: VPC Network & Database Schema Design (Weeks 1 - 2):** Initialize VPC, subnets, routing tables, and security groups. Establish DocumentDB database schemas.
2.  **Phase 2: Core API & Real-Time Setup (Weeks 3 - 5):** Build authentication mechanisms, catalog CRUD operations, SVG schematics, and Socket.io integration with Redis adapter.
3.  **Phase 3: Asynchronous Transaction Processing (Weeks 6 - 8):** Code Lambda webhooks, create SQS queue, write the backend worker consumer logic. Set up Dockerfiles.
4.  **Phase 4: Cloud Deployment & Load Testing (Weeks 9 - 11):** Deploy infrastructure using ECS Fargate, ALB, S3, CloudFront, and WAF. Run mock traffic load tests (1,000+ users), tune indexes, and complete project handover.

*Technical Requirements*  
- **Runtime:** Docker Engine for building, AWS CLI/CDK for infrastructure provisioning.
- **Frontend:** ReactJS + Vite + Tailwind CSS, `socket.io-client`.
- **Backend:** NodeJS + ExpressJS, Mongoose client, `vnpay` integration, `axios` HTTP library.

### 5. Timeline & Milestones  
- **Milestone 1 (Weeks 1 - 2):** VPC infrastructure completed, DocumentDB cluster initialized, user Auth APIs functioning.
- **Milestone 2 (Weeks 3 - 5):** Front page, interactive schematics viewer, and support chat rooms fully implemented.
- **Milestone 3 (Weeks 6 - 8):** AI Image Scan features active. Automated IPN payment queues via Lambda and SQS deployed.
- **Milestone 4 (Weeks 9 - 10):** ECS Fargate scaling active, React bundle deployed to S3 and served via CloudFront + WAF.
- **Milestone 5 (Week 11):** Completed load tests, database query index optimizations, and project handover.

### 6. Budget Estimation  
Estimated monthly AWS production infrastructure budget:

| AWS Service | Configuration Details | Monthly Cost (Est.) |
| :--- | :--- | :--- |
| **Amazon ECS & Fargate** | 2 Tasks (0.5 vCPU, 1 GB RAM) | ~ $15.00 |
| **Application Load Balancer** | 1 ALB, 1 LCU | ~ $22.00 |
| **Amazon DocumentDB** | db.t3.medium Cluster (1 Primary + 1 Replica) | ~ $110.00 |
| **Amazon ElastiCache Redis** | cache.t3.micro Cluster (1 Primary + 1 Replica) | ~ $30.00 |
| **Amazon S3** | Static Hosting & Media Storage (~ 50 GB) | ~ $3.00 |
| **Amazon CloudFront** | Outbound data transfer (~ 150 GB) | ~ $12.00 |
| **AWS WAF** | 1 Web ACL + 3 Basic Rule Groups | ~ $10.00 |
| **NAT Gateways** | 2 NAT Gateways + network transfer fees | ~ $65.00 |
| **AWS Lambda & SQS** | 50,000 transactions (Free Tier eligible) | ~ $0.00 |
| **Total Infrastructure Cost** | **Production-grade Environment** | **~ $267.00 / Month** |

### 7. Risk Assessment  
*Risk Matrix & Mitigation Strategies*  
1.  **Database query latency under peak loads:**
    *   *Risk:* Flash sale campaigns overload DocumentDB CPU with product details reads.
    *   *Mitigation:* Route all read queries to DocumentDB replica instances and cache popular products in Redis.
2.  **WebSocket connection dropping during backend auto-scaling:**
    *   *Risk:* Container scaling events disconnect ongoing support chats.
    *   *Mitigation:* Enable Sticky Sessions in ALB to lock connection endpoints, backed by Redis Pub/Sub adapter to sync state across tasks.
3.  **Out-of-control AWS billing:**
    *   *Risk:* High traffic or incorrect Fargate parameters spike monthly cost.
    *   *Mitigation:* Configure AWS Budgets to alert administrators immediately when monthly forecasts exceed $300. Set S3 lifecycle rules to purge old AI Scan logs.

### 8. Expected Outcomes  
*   **Technical Goals:** Global page loading times below 2 seconds. Auto-scaling capability (2 to 10 tasks) to handle traffic spikes. 99.99% service availability.
*   **Business Impact:** Zero lost transaction logs during gateway timeouts. Lower customer drop-off rates through engaging UI features (Schematics & AI image scanning). projects.