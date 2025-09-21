---
- title: "TDCOA: Transforming Telemetry and Usage Analytics -- Teradata"  
- description: "As Global Director at Teradata, tackled inconsistent telemetry and reporting with POC project: TDCOA. Gathered best in class metrics, simplified and centralized collection, built Python framework for automated analytics and PPTX. Saved $17M annually in time savings, standardized reporting, improved customer perception, and influenced future SaaS evolution."  
- image: "bizstory-generic.png"  
- author: "Stephen Hilton"  
- date: true  
- keywords: "aws loop, projects, learnings"  
- navs: ["top"]  
- highlights:
    - Ownership: Initiated and led TDCOA to address telemetry inefficiencies.  
    - Customer Obsession: Improved customer experience with consistent, standardized reporting.  
    - Dive Deep: Consolidated metrics, partnered with engineers, built telemetry-over-support pipeline.  
    - Invent and Simplify: Created Python framework automating analytics, charting, and PPTX generation.  
    - Deliver Results: Saved 24hrs per SA/CSM monthly, aka $12M/yr, and improving over time with SaaS evolution.  
    - Earn Trust: Gained adoption from senior SAs, reinforced credibility with leadership.  
---

# Overview

### Situation:
- Teradata telemetry collection and usage analytics highly inefficient
- No centralized collection; on-premise legacy architecture persisted into SaaS model
- No standard metrics; inconsistent queries and results among SAs
- No guidance on presenting/using findings with customers
- Result: confusion, inconsistent internal/external reporting, poor customer perception

### Tactics:
- Built plan and garnered approval from CCO (manager):
    - Gather best-in-class telemetry metrics/analytics from senior SAs & CSMs
    - Vet metrics with platform engineers for accuracy/applicability
    - Partner with product engineering to collect telemetry via support infrastructure
    - Develop Python POC framework (TDCOA) for automated analytics and PPTX
- If successful, request engineering investment to scale solution

### Actions:
- Interviewed SE/CSM/Sales leadership for most effective usage analytic metrics / reports
- Consolidated and de-duplicated,
- Spend day with product engineering to vet and rationalize all metrics
- Built POC: automated connection, analytics, visualizations, and PPTX generation
- In parallel, worked with Product Eng. on centralized telemetry sourcing
- Once done, demo’d to CCO, secured approval and budget to scale
- Hardened and scaled TDCOA:
    - Allow for edge cases (no outside access, or telemetry over support)
    - Distribution over github / pypi.org for OS agnostic
    - Better UI (still internal tool)
    - Supported extensibility to continue SE innovation / bespoke customer reports 
    - One SE developed graphing network of table joins by schema
- Rolled out first to senior SAs for UAT and to accelerate adoption
- Provided office hours, training, and regional presentations 

### Results:
- Saved 16–24hrs per SA/CSM monthly (~$17M annual savings)
- Improved consistency and credibility of reporting across Teradata
- Enhanced customer experience with standardized, clear analytics
- Expanded to Success Plans, competitive decks, bespoke customer reports
- Enabled strategic messaging at leadership level
- SaaS evolution continued based on telemetry-over-support foundation
- FYI: Validated technical design; similar to DBT’s SQL + Jinja approach

---

# Customer Obsession:
Consistency, automation, and credibility in telemetry analytics.

- **Ownership** – Initiated and led TDCOA to address telemetry inefficiencies.  
- **Customer Obsession** – Improved customer experience with consistent, standardized reporting.  
- **Dive Deep** – Consolidated metrics, partnered with engineers, built telemetry-over-support pipeline.  
- **Invent and Simplify** – Created Python framework automating analytics, charting, and PPTX generation.  
- **Deliver Results** – Saved $17M/year, 24hrs per SA/CSM monthly, validated by SaaS evolution.  
- **Earn Trust** – Gained adoption from senior SAs, reinforced credibility with leadership.  

[Back to the project index page](/projects.html).

---

# Full Text
All organizations contend with change and challenge; even the most astute and prepared companies are continually adjusting to fit within the context of a changing world. At my tenure at Teradata, first as a Sr. Solution Engineer (SE/SA) then 6 years as a Director of SalesTech (combined SAs and CSM organization), one particularly painful inefficiency stood out as cumbersome: telemetry collection and usage analytics.

The challenge had three major components:  
**No Centralized / Automated Collection** – Because Teradata evolved from an on-premise delivery model, system telemetry data was still written to local servers. This offered high fidelity data in an isolated environment, but access required direct system connectivity, granted by the customer. Some SAs had access, however many did not, and no central repository existed for cross-platform comparisons. This problem persisted even as Teradata transitioned into a Cloud / SaaS model.  
**No Standard Metrics** – SAs fortunate enough to have access were offered no guidance on synthesizing that data into metrics meaningful to customers. At best, new SAs could ask senior SAs/mentors for their particular flavor of metrics; at worst, they started building their own from scratch.  
**No Guidance on Applying / Presenting Findings** – Once the SA could generate directionally accurate metrics, they still had no guidance on how to use these measures to guide their customers and internal partners.

The combined outcome was frequent confusion: internal sales leaders had no aggregate view of customer usage. SAs on internal calls presented different usage measures depending on the customer, sometimes squabbling over accuracy. Worst of all, when an SA was re-assigned, they brought along a new set of “best practices,” causing resets in planning and expectations, damaging customer perception.

When I was promoted to the Global Director of Strategy, Analytics, and Automation for SalesTech, this was one of the first challenges I set out to address. After discussions with the Chief Customer Officer (my direct manager), I constructed and executed a plan with parallel activities.  

First, I gathered best-in-class telemetry metrics, analytics, and presentations from the most senior SAs and CSMs. With field findings in-hand, I vetted metrics with lead platform engineers for technical accuracy and customer applicability, arriving at a “best-of-the-best” set of analytics.  

In parallel, I worked with product engineering to begin centrally collecting telemetry via support infrastructure. This low-bandwidth connection required optimizing metrics within available bandwidth, pre-aggregating analytics, and collecting centrally. I partnered with legal to update terms of service for compliance.  

With the above in progress, I developed a Python POC framework that became TDCOA. The framework guided SAs through system connection, executed analytic queries, and generated charts, graphs, and PPTX output. It identified anomalies, generated recommendations, and provided talking points—all in minutes.  

I presented the demo to the CCO with proposals and value propositions. Estimated cost savings: ~$1M/month from 400 SAs/CSMs saving 16hrs each, at $150/hr. Requested 4 months of engineering effort to scale product. Recoup time: 3 days post-deployment. Approved in full.  

Over the next 4 months, I matured TDCOA with my engineering team. We added auto-update capabilities, edge-case support, and custom template options. One SA created a network graph template showing schema relationships, enabling new customer insights.  

Rollout began with senior SAs for rigorous UAT and influence. Adoption spread smoothly across regions, supported by office hours and team presentations. Within 18 months, templates expanded to Success Plans, competitive decks, and bespoke reports. Savings reached ~$17M annually, not counting efficiency gains.  

Three years later, colleagues report the telemetry-over-support infrastructure remains foundational, with TDCOA largely replaced by centralized SaaS tools, still using the same analytics and outputs—a natural evolution.  

**Technical epilogue:** TDCOA combined Teradata SDK, pandas/numpy, seaborn, pyPPTX, and Jinja2 templating for SQL and Python scripts. About 12 months after release, DBT appeared with SQL + Jinja pipelines, validating TDCOA’s design.  
