---
title: "Week 11 Worklog"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.11. </b> "
---
{{% notice warning %}} 
⚠️ **Note:** The following information is for reference purposes only. Please **do not copy verbatim** for your own report, including this warning.
{{% /notice %}}


### Week 11 Objectives:

* Develop the Admin Dashboard panel governing product list updates, client orders, and coupon vouchers.
* Embed Recharts analytical widgets for visualizing business statistics like revenue streams and order count trends.
* Design admin-facing chat logs checking panel.
* **AWS Integration:** Enforce security checking on Admin Dashboard API calls via AWS ALB using JWT token validation.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Develop inventory manager console (add/edit/delete product items, updating size dimensions and attributes) | 06/29/2026 | 06/29/2026 | NodeJ2Car layout specs |
| 3 | - Build orders control view (updating dispatch status, tracking client payment details) | 06/30/2026 | 06/30/2026 | NodeJ2Car API documentation |
| 4 | - Construct discount coupons campaign creator, establishing code patterns and validation criteria | 07/01/2026 | 07/01/2026 | Figma coupon designs |
| 5 | - Embed Recharts library graph components mapping transaction metrics and order growth patterns | 07/02/2026 | 07/02/2026 | Recharts API documentation |
| 6 | - Design Customer Service Inbox interface for administrator chats <br> - **AWS Integration:** Validate administrative REST queries directed to ECS Backend containers through ALB, ensuring JWT check enforcement | 07/03/2026 | 07/03/2026 | AWS ALB routing security guides |

### Week 11 Achievements:

* Built functional Admin Dashboard boasting clean layouts and structured catalog modifiers.
* Integrated responsive Recharts components simplifying raw revenue analytical tracking on UI.
* Rolled out administrator chat inbox receiving real-time client questions instantly.
* Verified that admin queries require active JWT roles, with ALB filtering out unauthorized traffic at the border.
