---
title: "Week 5 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.5. </b> "
---
{{% notice warning %}} 
⚠️ **Note:** The following information is for reference purposes only. Please **do not copy verbatim** for your own report, including this warning.
{{% /notice %}}


### Week 5 Objectives:

* Study in-depth advanced AWS storage solutions (S3 Access Points, Storage Classes, Glacier, Snow Family) and perform virtual machine migration from on-premises (VM Import/Export).
* Deploy high-performance Multi-AZ FSx for Windows File Server (SSD/HDD FSx, Shadow copies, Quotas, Data deduplication) and AWS Storage Gateway.
* Research AWS security models (Shared Responsibility, IAM, Cognito, AWS Organizations, Identity Center, KMS, Security Hub).
* Manage AWS resource tagging and automate EC2 operations (Lambda auto start/stop EC2 based on tags, Slack notifications).
* Configure fine-grained access policies using IAM Policies/Roles, restrict Switch Role access by IP & Time, use KMS encryption, and audit activity using CloudTrail and Amazon Athena.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **Advanced Storage & Migration:** <br>&emsp; + Module 04-01 -> 04-04: AWS Storage services theory <br>&emsp; + Module 04-Lab14-01 -> Lab14-05: VM Import/Export virtual machine from on-premises to AWS <br>&emsp; + Module 04-Lab13-02.1 -> Lab13-06: Advanced AWS Backup configurations | 05/18/2026 | 05/18/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Enterprise File Sharing Systems:** <br>&emsp; + Module 04-Lab24-2.1 -> Lab24-3: Storage Gateway and local file share mounting <br>&emsp; + Module 04-Lab25-2.2 -> Lab25-13: SSD/HDD Multi-AZ FSx Windows File Server, shadow copies, quotas, and data deduplication <br>&emsp; + Module 04-Lab57-2.1 -> Lab57-11: Advanced S3 Static Website & CloudFront | 05/19/2026 | 05/19/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Infrastructure Security & Operations Automation:** <br>&emsp; + Module 05-01 -> 05-08: AWS Security theory <br>&emsp; + Module 05-Lab18-02 -> Lab18-04: Evaluate security posture using AWS Security Hub <br>&emsp; + Module 05-Lab22-2.1 -> Lab22-7: Create Lambda function to auto-start/stop EC2 by tag and trigger Slack webhook | 05/20/2026 | 05/20/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **Resource Tagging & Advanced IAM Controls:** <br>&emsp; + Module 05-Lab27-2.1.1 -> Lab27-4: Tag management & Resource Groups <br>&emsp; + Module 05-Lab28-2.1 -> Lab28-6: IAM Policies, Roles, Switch Roles <br>&emsp; + Module 05-Lab30-3 -> Lab30-6: Create Limited Users and policy boundaries <br>&emsp; + Module 05-Lab44-2 -> Lab44-5: Limit switch role access by IP and Time | 05/21/2026 | 05/21/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Encryption, Logging & Audits:** <br>&emsp; + Module 05-Lab33-2.1 -> Lab33-7: KMS encryption for S3, AWS CloudTrail logging, Amazon Athena querying <br>&emsp; + Module 05-Lab48-1.1 -> Lab48-4: Differentiate Access Key vs IAM Instance Profile (IAM Role) on EC2 | 05/22/2026 | 05/22/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Week 5 Achievements:

* Migrated physical/on-premises virtual machines to AWS Cloud successfully using VM Import/Export utilities.
* Set up a highly robust FSx for Windows File Server sharing network, enabling Windows Shadow copies for user recovery and Data Deduplication to save storage costs.
* Automated EC2 instance schedules (start/stop) off-business hours using Lambda and EventBridge rules based on tagging metadata, outputting instant status alerts to Slack channels.
* Audited account security posture against industry standards via AWS Security Hub.
* Managed security authorization profiles using custom IAM policies constraining Switch Role actions to designated VPN IP subnets and predefined working hours.
* Secured static assets with KMS customer-managed keys, recorded complete AWS API invocation footprints to S3 using CloudTrail, and performed log audits via SQL queries in Amazon Athena.
* Adopted standard security best practices by always configuring IAM Roles on EC2 hosts (IAM Instance Profiles) instead of provisioning hardcoded IAM Access Keys.
