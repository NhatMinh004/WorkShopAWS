---
title: "Week 13 Worklog"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.13. </b> "
---
{{% notice warning %}} 
⚠️ **Note:** The following information is for reference purposes only. Please **do not copy verbatim** for your own report, including this warning.
{{% /notice %}}


### Week 13 Objectives:

* Integrate AWS WAF (Web Application Firewall) to protect application endpoints from common web exploits.
* Configure Web ACLs on the CloudFront edge to block malicious traffic patterns and mitigate DDoS attempts.
* Establish rate limiting rules protecting authentication routes from brute force attempts.
* Implement AWS WAF Bot Control managed rulesets to filter automated vulnerability scanners.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Research AWS WAF concepts, including Web ACLs, Rules, and Managed Rule Groups | 07/13/2026 | 07/13/2026 | AWS WAF user guide |
| 3 | - Provision a Web ACL under the Global region and attach it to the project CloudFront Distribution | 07/14/2026 | 07/14/2026 | AWS WAF integration guides |
| 4 | - **Rate Limiting Rule Setup:** Build a rate limit rule to block IPs generating excessive requests, preventing application-layer DDoS | 07/15/2026 | 07/15/2026 | WAF rate limiting rules guide |
| 5 | - **Bot Control Policy:** Enable AWS Managed Rules Bot Control to classify and block automated crawler tools | 07/16/2026 | 07/16/2026 | WAF Managed Rules reference |
| 6 | - **Log Monitoring & Tuning:** Analyze blocked requests via sampled logs, tuning rules to eliminate false positives | 07/17/2026 | 07/17/2026 | AWS WAF logs dashboard |

### Week 13 Achievements:

* Successfully integrated AWS WAF filtering incoming HTTP requests at the CloudFront edge.
* Protected web endpoints against heavy scraping or request-based DDoS through automated IP rate limiting.
* Isolated and blocked automated bad crawler scripts, securing application APIs.
* Tuned rule exclusions to verify legitimate users bypass checks with zero latency penalties.
