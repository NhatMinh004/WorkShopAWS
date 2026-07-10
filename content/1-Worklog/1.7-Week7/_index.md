---
title: "Week 7 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---
{{% notice warning %}} 
⚠️ **Note:** The following information is for reference purposes only. Please **do not copy verbatim** for your own report, including this warning.
{{% /notice %}}


### Week 7 Objectives:

* Construct core storefront pages: Homepage, filter-enabled Shop page, and interactive vehicle Schematic view.
* Design technical Part Detail sheet, product Comparison panel, and user Wishlist.
* **AWS Integration:** Pull and display catalog images from S3 Media Bucket and optimize loading latency using Amazon CloudFront CDN.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Design Homepage (Home.jsx) presenting dynamic hero banners of highlighted parts and partner brands | 06/01/2026 | 06/01/2026 | NodeJ2Car layout wireframes |
| 3 | - Build Shop catalog page (Shop.jsx) with multi-criteria filters (price range, manufacturer, category) and client pagination | 06/02/2026 | 06/02/2026 | NodeJ2Car API documentation |
| 4 | - Program the interactive vehicle blueprint schematic (Schematic.jsx) allowing users to click SVG car components (e.g., brakes, engine) to query related parts | 06/03/2026 | 06/03/2026 | Car schematic SVG vector draft |
| 5 | - Construct technical Part Detail layout (PartDetail.jsx) hosting dimensions, compatibility lists, and user review modules | 06/04/2026 | 06/04/2026 | NodeJ2Car product schemas |
| 6 | - Develop side-by-side product Compare grid (Compare.jsx) and localStorage-backed favorite list (Wishlist.jsx) <br> - **AWS Integration:** Link product image assets stored in S3 Media Bucket optimized via Amazon CloudFront CDN caching | 06/05/2026 | 06/05/2026 | AWS CloudFront cache configuration |

### Week 7 Achievements:

* Completed storefront Homepage and filter-driven Shop catalog hooked dynamically to backend REST endpoints.
* Built interactive vehicle SVG Schematic parser, creating a unique navigation flow.
* Released comprehensive Part Detail page side-by-side comparison tables.
* Linked frontend asset bindings with centralized storage hosted on AWS S3 Media Bucket.
* Deployed CloudFront CDN distribution to cache catalog pictures, dropping homepage load duration significantly.
