--- 
- title: "10x Migration Debacle at $1B Manufacturer"  
- description: "Migration after competitive win, scoping error created ×10 workload admidst urgent timelines. Escalated to leadership, secured benched consultants and started automating migration tools. After 5mo of intense execution, delivered 4ks late but 10x scope, making project unprofiable but preserved customer trust, and developed new internal automation framework."  
- image: "bizstory-generic.png" # image file, as found in /src/images/ folder
- author: "Stephen Hilton" # author of the page, if applicable (should appear in footer)
# - date: true # if type date, use as-is.  If "true", use date of last sitegen.py generation.
- keywords: "aws loop, projects, learnings" # SEO / metadata keywords
- navs: ["top"]  # navigation sections that wrap this page. Template for each should be included in /src/templates/navs/[nav].jinja
- highlights:
  - Ownership: Took responsibility as both PM and technical lead, escalated quickly, reallocated resources, drove execution despite not being part of original scoping.  
  - Bias for Action: Challenged leadership’s instinct to pause/re-scope, insisted on immediate forward motion, mobilized benched consultants within 24 hours.  
  - Dive Deep: Analyzed scoping error impact (child vs parent objects, 10x scope), broke work into modular components, worked with AB specialists to build automation framework.  
  - Invent and Simplify: Created bespoke automation tools for Ab Initio and Informatica migrations, enabling faster throughput despite expanded workload.  
  - Earn Trust: Communicated openly with customer CTO about issue and plan, demonstrated accountability and commitment to delivery.  
  - Deliver Results: Completed 10x original scope, only 25% late (4 weeks on a 4-month project), developed new migration automation capability, preserved customer satisfaction despite project unprofitability.  
  - Insist on the Highest Standards: Insisted on not pausing project to cast blame, but drive relentlessly to fast, high-quality outputs.
---

# Overview

### Situation:
- New customer – $1B/yr manufacturing company
- Just complted competitive POC of Hadoop + DBMS (load 10M rows < 1sec) 
- Led migration project as PM + SE -- new systems, biz, CTO
- I did not do migration project scoping
- As project got going, migration Eng. raised concern about project scope
  - scoped on Plan object, not child "Graph" - 10x difference!

### Tactics:
- Project was time-sensitive (4mo), with dependencies
- Needed to pull together our plan rapidly 

### Actions:
- Morning after discovery, call with head of consulting to “borrow” all benched PS
  - He and I built a plan to automate with experts, disseminate work where we could not
  - Pulled experts: 2 AB, 1 Infra, 1 PM (freeing me as Techlead)
- By afternoon, call with Sales LT to co-present with Consulting + SE, got approval (RedHIP)
  - Root-cause could wait (imperative, not time sensitive)
- By evening, plan was in motion, internal docs, customer preso 
- Next morning was emergency meeting with CTO & team
  - Explained problem, what we’re doing, timeline, etc. – without admitting fault
  - Tense meetings, but appreciated our response
  - Root-cause could wait (imperative, not time sensitive)
- Next few days, build a plan and onboarded consultants, including 2 AB and 1 Infra, and 1 PM
- Offloaded PM work to PM, so I could go deep-heads-down
- Next week, worked with AB folks to build automated migration framework

### Results:
-	We delivered 4 weeks late (5mo total, +25%), but delivered 10x the work
-	We did post-mortem; customer mislabeled, but we didn’t catch (pressure to go fast)
-	We were RedHip, but customer eventually agreed to pay addition $50k to bring us to break-even
-	Developed new AB migration automation, for migration team
-	Customer was happy with result & trusted us to deliver

---

# Customer Obsession:
Protected first impression, prioritized customer delivery.

- **Ownership** – Took responsibility as both PM and technical lead, escalated quickly, reallocated resources, drove execution despite not being part of original scoping.  
- **Bias for Action** – Challenged leadership’s instinct to pause/re-scope, insisted on immediate forward motion, mobilized benched consultants within 24 hours.  
- **Dive Deep** – Analyzed scoping error impact (child vs parent objects, 10x scope), broke work into modular components, worked with AB specialists to build automation framework.  
- **Invent and Simplify** – Created bespoke automation tools for Ab Initio and Informatica migrations, enabling faster throughput despite expanded workload.  
- **Earn Trust** – Communicated openly with customer CTO about issue and plan, demonstrated accountability and commitment to delivery.  
- **Deliver Results** – Completed 10x original scope, only 25% late (4 weeks on a 4-month project), developed new migration automation capability, preserved customer satisfaction despite project unprofitability.  
- **Insist on the Highest Standards** – Insisted on not pausing project to cast blame, but drive relentlessly to fast, high-quality outputs.

[Back to the project index page](/projects.html).

---

# Full Text
I was running a net-new customer migration project as both the technical lead and the project manager (PM). Normally we'd assign a dedicated PM, however, I was very familiar with the business having successfully won the business via a competitive POC. I knew the business, all technical infrastructure and data pieces, but also I knew the CTO and his entire team, and the project requirements start-to-finish. 

I was not however part of the project scoping. As we progressed, it became apparent that the scoping was incorrect - the scoping team had asked for a unit of work at the “child” level, the customer had provided it at the “parent” level. This meant the scope was off by 10x! As the project was time-sensitive, overnight it became very likely we’d miss the delivery date, and trigger a series of dependent project delays. 

I immediately escalated to internal leadership. They initially wanted to pause and re-scope, however I explained that would only increase delays – regardless of how we overcame the challenge, moving forward quickly was paramount. This was a new customer, and we didn’t want our first impression to be of a massively delayed project. Leadership came to agree, and allowed me to re-allocate every benched developer not already on a project (and a few who were). The following day, I went back to the customer CTO and explained what had happened, that I didn’t have an adjusted timeline yet, but that I had pulled every single resource I could, and had already broken the work into modular components in an attempt to keep as close to their original deadline as possible. I also had pulled in a couple of partner product engineers to perform some migration automation, so we could accelerate the work through clever automation. 

In the end, we were over-time by around 25% (4wks over a 4mo project), however, had completed almost 10x more work. The project was no longer profitable, however we saved the customer experience and demonstrated our commitment to good customers.  

Back to the [project index page](/projects.html).