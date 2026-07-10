---
title: "Week 8 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.8. </b> "
---
{{% notice warning %}} 
⚠️ **Note:** The following information is for reference purposes only. Please **do not copy verbatim** for your own report, including this warning.
{{% /notice %}}


### Week 8 Objectives:

* Develop the Cart management module and code checkout navigation flows.
* Embed Leaflet maps into the shipping configuration views to pin customer address geographical coordinates.
* Build the order summary review panel (PlaceOrder).
* **AWS Integration:** Test checkout order requests submitted over secure HTTPS passing through AWS Application Load Balancer (ALB) to ECS Backend.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Code the Cart layout (Cart.jsx) controlling items list, modifying quantities, removing items, and redeeming discounts coupons | 06/08/2026 | 06/08/2026 | NodeJ2Car layout wireframes |
| 3 | - Design client shipping form (Shipping.jsx) to collect contact name, phone, and delivery option indicators | 06/09/2026 | 06/09/2026 | NodeJ2Car API documentation |
| 4 | - Embed Leaflet interactive maps library (react-leaflet) in Shipping.jsx to pinpoint geographical coordinates for delivery | 06/10/2026 | 06/10/2026 | Leaflet API docs |
| 5 | - Construct PlaceOrder review board (PlaceOrder.jsx) calculating taxes, delivery surcharges, and order totals | 06/11/2026 | 06/11/2026 | Figma checkout templates |
| 6 | - **AWS Integration:** Implement and verify HTTPS transmission of checkout requests to ECS Backend hosts sitting behind Application Load Balancer (ALB) | 06/12/2026 | 06/12/2026 | AWS ALB SSL setup |

### Week 8 Achievements:

* Finished client-side Cart module caching selected products to prevent loss on browser reloads.
* Ticked off react-leaflet map integration enabling graphical pinning of addresses, reducing delivery coordinates input friction.
* Integrated dynamic PlaceOrder calculator outputting precise values synced directly with Stripe/COD backend parameters.
* Deployed secure HTTPS routing through ALB, defending sensitive checkouts from potential eavesdropping.
