---
title: "Week 6 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---
{{% notice warning %}} 
⚠️ **Note:** The following information is for reference purposes only. Please **do not copy verbatim** for your own report, including this warning.
{{% /notice %}}


### Week 6 Objectives:

* Initialize React/Vite boilerplate structure and configure Tailwind CSS along with routing architecture.
* Build Register & Login screens optimized with responsive styling for mobile platforms.
* Set up global user authentication state management via AuthContext and Axios Interceptors handling JWT tokens.
* Verify API routing and CORS policies using AWS Application Load Balancer (ALB).

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Initialize React project using Vite build tool <br> - Set up Tailwind CSS, components.json, and establish color palette and typography unique to NodeJ2Car branding | 05/25/2026 | 05/25/2026 | NodeJ2Car project documentation |
| 3 | - Configure static and dynamic client-side routes using react-router-dom <br> - Construct baseline layouts (Header, Footer, Sidebar) <br> - Setup environment files (.env.development) and parameters | 05/26/2026 | 05/26/2026 | NodeJ2Car routing layout specs |
| 4 | - Develop responsive authentication pages for registration (Register.jsx) and login (Login.jsx) supporting mobile devices | 05/27/2026 | 05/27/2026 | Figma design guidelines |
| 5 | - Integrate Axios library for HTTP network calls <br> - Implement Axios Interceptors to automatically append JWT Authorization headers on backend queries | 05/28/2026 | 05/28/2026 | NodeJ2Car API documentation |
| 6 | - Develop global login state manager utilizing AuthContext <br> - **AWS Integration:** Test authentication API requests through AWS Application Load Balancer (ALB) to check CORS configurations | 05/29/2026 | 05/29/2026 | AWS ALB guides |

### Week 6 Achievements:

* Successfully initialized the React/Vite boilerplate with clean directory organization and integrated Tailwind CSS configurations.
* Completed baseline client-side navigation paths and central application layouts.
* Released fully responsive Login and Register screens featuring robust form inputs validation rules.
* Established secure client session management storing JWT tokens in AuthContext, automatically attaching authorization parameters on outgoing Axios calls.
* Resolved client CORS exceptions by verifying requests successfully from the frontend through AWS Application Load Balancer (ALB).
