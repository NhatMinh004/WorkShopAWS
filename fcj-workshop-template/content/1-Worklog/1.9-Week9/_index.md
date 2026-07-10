---
title: "Week 9 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.9. </b> "
---
{{% notice warning %}} 
⚠️ **Note:** The following information is for reference purposes only. Please **do not copy verbatim** for your own report, including this warning.
{{% /notice %}}


### Week 9 Objectives:

* Integrate AI-powered broken auto part scanning interface (AI Scan UI) and bind mobile cameras.
* Design payment method selection gateway, executing redirects to VNPay, MoMo, and Stripe hosts.
* Implement transaction feedback page (OrderResult) parsing query URL parameters to display dynamic payment alerts.
* **AWS Integration:** Store scanning images to AWS S3 Media Bucket and configure AWS Lambda webhook triggers to sync order states over IPN.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Design photograph snapping/upload triggers in search widgets and product details <br> - Configure HTML5 media capture interface querying hardware cameras | 06/15/2026 | 06/15/2026 | MDN MediaStream API |
| 3 | - Program Skeleton Loading structures and micro-animations mirroring AI analysis duration <br> - Populate lists of detected automobile parts and matching parts catalog | 06/16/2026 | 06/16/2026 | Figma CSS transitions guides |
| 4 | - **AWS Integration (S3):** Configure frontend SDK bindings transmitting snapped photographs to AWS S3 Media Bucket to persist image search history | 06/17/2026 | 06/17/2026 | AWS S3 PutObject reference |
| 5 | - Construct checkout payment panel (Payment.jsx) <br> - Code client redirects to third-party bank gateways (Stripe, VNPay, MoMo) | 06/18/2026 | 06/18/2026 | Stripe checkout guides |
| 6 | - Build checkout success/failure landing board (OrderResult.jsx) parsing gateway redirect queries <br> - **AWS Integration (Lambda):** Verify order lifecycle syncing driven by AWS Lambda webhook handler IPN events | 06/19/2026 | 06/19/2026 | AWS Lambda triggers handbook |

### Week 9 Achievements:

* Built functional AI Scan camera framework compatible with Android/iOS WebViews.
* Integrated Skeleton loader layouts smoothing wait states during image processing.
* Configured automated image uploads mapping to Amazon S3 folders.
* Handled VNPay, MoMo, and Stripe redirection loops securely.
* Programmed OrderResult parameter parser synced with Lambda IPN webhook events, refreshing payment outcome on client interface without delay.
