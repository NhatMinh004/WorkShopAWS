---
title: "Week 10 Worklog"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 1.10. </b> "
---
{{% notice warning %}} 
⚠️ **Note:** The following information is for reference purposes only. Please **do not copy verbatim** for your own report, including this warning.
{{% /notice %}}


### Week 10 Objectives:

* Integrate real-time chat (Real-time Chat) and instant notifications (Notification System) using WebSockets.
* Build floating customer Chat widgets and corresponding admin panel chat dashboard.
* **AWS Integration:** Route WebSocket traffic through AWS Application Load Balancer (ALB) backed by Sticky Sessions for persistent connectivity.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Install socket.io-client library to initiate dynamic WebSocket handshake with Backend | 06/22/2026 | 06/22/2026 | Socket.io Client manuals |
| 3 | - Develop floating Chat UI widget positioned at the bottom right corner for customer-to-staff interaction | 06/23/2026 | 06/23/2026 | NodeJ2Car chat layouts |
| 4 | - Construct Admin Chat dashboard (admin/chat) enabling customer support representatives to handle concurrent threads | 06/24/2026 | 06/24/2026 | NodeJ2Car admin UI mockup |
| 5 | - Program real-time incoming messages handler and notification badges on main application Header | 06/25/2026 | 06/25/2026 | React state management guides |
| 6 | - **AWS Integration:** Align socket.io client connection settings with AWS ALB Sticky Sessions target group configurations to lock handshakes to identical ECS container instances | 06/26/2026 | 06/26/2026 | AWS ALB WebSocket guidelines |

### Week 10 Achievements:

* Integrated socket.io-client connectivity successfully, establishing sub-second real-time messaging pipeline.
* Released clean Chat widgets on client and admin sections supporting emoji inputs.
* Implemented live notification badges updating automatically on new chat alerts.
* Hardened WebSocket stability by enforcing ALB Sticky Sessions, eliminating unexpected client disconnects across backend container tasks.
