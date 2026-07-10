---
title: "Week 12 Worklog"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.12. </b> "
---
{{% notice warning %}} 
⚠️ **Note:** The following information is for reference purposes only. Please **do not copy verbatim** for your own report, including this warning.
{{% /notice %}}


### Week 12 Objectives:

* Compile React SPA (Vite) bundle and deploy assets to AWS S3 Static Website Hosting under SSL/HTTPS on CloudFront CDN.
* Integrate AWS WAF policies filtering DDoS attempts and scanning bots.
* Evaluate client performance using Google Lighthouse metrics and optimize SEO components.
* Design custom CloudFront Cache-Control configurations, conduct end-to-end integration tests, and finalize project handoff.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Compress static images, strip debug traces, and execute code splitting <br> - Run `npm run build` command compiling React source tree into `/dist` output | 07/06/2026 | 07/06/2026 | Vite compilation handbook |
| 3 | - **AWS S3 & CloudFront Deployment:** Publish compilation artifacts to S3 bucket, enabling website hosting. Spin up CloudFront Distribution pointing to S3 origin, configure custom index routing fallbacks, and bind ACM certificates | 07/07/2026 | 07/07/2026 | AWS S3/CloudFront guides |
| 4 | - **AWS WAF Integration:** Build WAF rule policies blocking automated vulnerability scanning bots, attaching rules to CloudFront CDN endpoints | 07/08/2026 | 07/08/2026 | AWS WAF configuration guides |
| 5 | - Audit Core Web Vitals using Google Lighthouse diagnostics <br> - Configure metadata, meta description tags, and Open Graph attributes for social media card previews | 07/09/2026 | 07/09/2026 | Google Lighthouse handbook |
| 6 | - **AWS Cache-Control:** Declare Cache-Control header instructions (CSS/JS cache duration, index.html no-cache rule) <br> - Perform complete End-to-End verification loops: Registration -> AI Scan -> Checkout -> Chat Widget and complete handoff | 07/10/2026 | 07/10/2026 | Integration test sheets |

### Week 12 Achievements:

* Built optimized SPA bundle, reducing download sizing by 35% through asset splitting.
* Launched production web storefront over HTTPS linked to a dedicated custom domain through CloudFront.
* Configured AWS WAF rules successfully blocking automated bad bot spiders.
* Achieved Google Lighthouse Performance scores exceeding 92 on mobile devices, with fully formatted social media share previews.
* Configured custom Cache-Control headers ensuring immediate cache invalidation for updated UI releases.
* Successfully handed over NodeJ2Car project meeting all performance targets.
