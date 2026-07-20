---
title: "Week 14 Worklog"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.14. </b> "
---
{{% notice warning %}} 
⚠️ **Note:** The following information is for reference purposes only. Please **do not copy verbatim** for your own report, including this warning.
{{% /notice %}}


### Week 14 Objectives:

* Auditing and optimizing Frontend web performance using Google Lighthouse diagnostics (Core Web Vitals).
* Configure SEO metadata tags and Open Graph properties for rich social media card sharing.
* Establish custom S3 metadata and CloudFront Cache-Control policies to reduce page loading latencies.
* Define Cache Invalidation procedures to guarantee immediate UI updates on new releases.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Run initial Google Lighthouse performance audits, logging LCP, CLS, and TBT scores to plan optimization targets | 07/20/2026 | 07/20/2026 | Google Lighthouse guide |
| 3 | - Perform code optimizations: compress images into WebP format and deploy lazy loading on heavy components | 07/21/2026 | 07/21/2026 | Web performance standards |
| 4 | - Integrate dynamic page titles, SEO description meta tags, and configure Facebook/Twitter Open Graph details | 07/22/2026 | 07/22/2026 | SEO integration handbook |
| 5 | - **AWS Cache-Control:** Declare Cache-Control header rules on S3 object metadata (long-lived CSS/JS assets, index.html no-cache rule) | 07/23/2026 | 07/23/2026 | S3 object metadata guides |
| 6 | - **CloudFront Invalidation:** Spin up Cache Invalidation tasks in the AWS Console, validating hotfix delivery in browser sessions | 07/24/2026 | 07/24/2026 | CloudFront caching controls |

### Week 14 Achievements:

* Boosted Google Lighthouse Performance diagnostics to scores exceeding 92 on both mobile and desktop views.
* Social media share queries dynamically extract clear catalog details (image, title, price) via Open Graph tags.
* Page loading latency on repeat visits decreased by over 50% through optimized browser caching.
* Guaranteed instantaneous updates on the client UI using the no-store directive on the entrypoint index.html file.
