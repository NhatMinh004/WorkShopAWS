---
title: "Week 4 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---
{{% notice warning %}} 
⚠️ **Note:** The following information is for reference purposes only. Please **do not copy verbatim** for your own report, including this warning.
{{% /notice %}}


### Week 4 Objectives:

* Understand advanced EC2 compute features in detail, including Instance Types, AMI, EBS, Instance Store, User Data, Metadata, and Auto Scaling.
* Deploy automated backup policies using AWS Backup.
* Design a hybrid storage environment via AWS Storage Gateway linking on-premises servers to S3.
* Set up a highly secure static website on S3 combined with Amazon CloudFront CDN.
* Learn and configure S3 Bucket Versioning and Cross-Region Replication (CRR).

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **In-depth EC2 Research:** <br>&emsp; + Module 03-01 - Compute VM on AWS <br>&emsp; + Module 03-01-01 - Instance type <br>&emsp; + Module 03-01-02 - AMI / Backup / Key Pair <br>&emsp; + Module 03-01-03 - Elastic block store <br>&emsp; + Module 03-01-04 - Instance store <br>&emsp; + Module 03-01-05 - User data <br>&emsp; + Module 03-01-06 - Meta data <br>&emsp; + Module 03-01-07 - EC2 auto scaling <br>&emsp; + Module-03-02 - EC2 Autoscaling - EFS/FSx - Lightsail - MGN | 05/11/2026 | 05/11/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Practice AWS Backup Lab:** <br>&emsp; + Module 03-Lab13-01 - Deploy AWS Backup - Introduction <br>&emsp; + Module 03-Lab13-02.2 - Deploy infrastructure <br>&emsp; + Module 03-Lab13-03 - Create Backup plan <br>&emsp; + Module 03-Lab13-05 - Test Restore <br>&emsp; + Module 03-Lab13-06 - Clean up resources | 05/12/2026 | 05/12/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Practice Storage Gateway Lab:** <br>&emsp; + Module 03-Lab24-01.1 - Create S3 Bucket <br>&emsp; + Module 03-Lab24-01.2 - Create EC2 for Storage Gateway <br>&emsp; + Module 03-Lab24-02.1 - Create Storage Gateway <br>&emsp; + Module 03-Lab24-02.2 - Create File Shares | 05/13/2026 | 05/13/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **Implement S3 Static Website:** <br>&emsp; + Module 03-Lab57-02.1 - Create S3 bucket <br>&emsp; + Module 03-Lab57-02.2 - Load data <br>&emsp; + Module 03-Lab57-03 - Enable static website feature <br>&emsp; + Module 03-Lab57-04 - Configuring public access block <br>&emsp; + Module 03-Lab57-05 - Configuring public objects <br>&emsp; + Module 03-Lab57-06 - Test website | 05/14/2026 | 05/14/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Configure S3 & CloudFront Advanced Settings:** <br>&emsp; + Module 03-Lab57-07.1 - Block all public access <br>&emsp; + Module 03-Lab57-07.2 - Config Amazon CloudFront <br>&emsp; + Module 03-Lab57-07.3 - Test Amazon Cloudfront <br>&emsp; + Module 03-Lab57-08 - Bucket Versioning <br>&emsp; + Module 03-Lab57-09 - Move objects <br>&emsp; + Module 03-Lab57-10 - Replication Object multi Region <br>&emsp; + Module 03-Lab57-11 - Clean up resources | 05/15/2026 | 05/15/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Week 4 Achievements:

* Acquired deep knowledge of EC2 instance types (compute-optimized, memory-optimized, storage-optimized) and differentiated between persistent EBS volumes and high-speed temporary Instance Store volumes.
* Configured User Data scripts to run boot tasks automatically and retrieved instance metadata via the CLI.
* Successfully set up automatic Backup Plans and verified system restoration using AWS Backup.
* Built a hybrid File Gateway system mapping local on-premises network drives to S3 buckets.
* Deployed an S3 hosted static site, restricted direct public traffic on the bucket, and routed requests through CloudFront CDN to safeguard data and accelerate load speeds globally.
* Implemented S3 Bucket Versioning to store previous file copies and set up Cross-Region Replication (CRR) to support disaster recovery (DR) plans.
