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

* Compile optimized React SPA (Vite) static build assets.
* Deploy static assets to AWS S3 Static Website Hosting.
* Initialize and configure AWS CloudFront Distribution for global edge delivery.
* Request SSL/TLS certificates from AWS Certificate Manager (ACM) to support HTTPS on custom domains.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Compress static images, strip debug traces, and execute code splitting <br> - Run `npm run build` command compiling React source tree into `/dist` output | 07/06/2026 | 07/06/2026 | Vite compilation handbook |
| 3 | - **AWS S3 Deployment:** Upload static assets to S3 Web Bucket, enable Static Website Hosting, and set Bucket Policy allowing CloudFront OAI/OAC access | 07/07/2026 | 07/07/2026 | AWS S3 documentation |
| 4 | - **CloudFront CDN Setup:** Establish CloudFront Distribution mapping to S3 origin, configuring Custom Error Responses (403/404) to fallback to index.html for React routing | 07/08/2026 | 07/08/2026 | AWS CloudFront guides |
| 5 | - **ACM SSL Certificate:** Request a public SSL/TLS certificate from ACM for the custom internship subdomain, validating via DNS CNAME verification | 07/09/2026 | 07/09/2026 | AWS ACM user guide |
| 6 | - **Domain Binding & Verification:** Bind ACM SSL certificate and custom domain to the CloudFront distribution, verifying endpoint routing over HTTPS | 07/10/2026 | 07/10/2026 | Route 53 DNS settings |

### Week 12 Achievements:

* Built optimized React bundle, dropping the initial load footprint by 35% through bundle split strategies.
* Hosted the static website files securely under S3 Web bucket integration.
* Configured CloudFront Custom Error Responses, preventing React Router sub-pages from failing with HTTP 403/404 on page refreshes.
* Secured transit channels with HTTPS, binding verified ACM certificates to custom subdomains.
