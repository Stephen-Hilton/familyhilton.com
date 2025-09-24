---
- title: "Compression Card Mis-Sizing: A Hard Lesson"  
- description: "As SE for a 1.2B user social media customer, discovered compression cards provided 40% less compression savings than CPUs, undersizing my system sizing. Worked with engineering to deliver custom fix (+15% free nodes) and shared mistake widely to prevent recurrence. Lesson: read technical docs carefully, and ask questions frequently."  
- image: "bizstory-generic.png"  
- author: "Stephen Hilton"  
- date: true  
- keywords: "aws loop, projects, learnings"  
- navs: ["top"]  
- highlights:
    - Ownership: Took responsibility for mis-sizing, drove resolution and shared lesson broadly.  
    - Customer Obsession: Ensured customer success by delivering extra nodes at no cost.  
    - Dive Deep: Validated compression issue through analysis and technical documentation.  
    - Earn Trust: Built credibility by openly admitting error across teams.  
    - Insist on the Highest Standards: Resolved to never skim new platform technical documentation again.  
    - Deliver Results: Delivered working system with custom solution, avoided repeated costly mistakes.  
---

# Overview

### Situation:
- Role: SE covering professional social media customer with 1.2B users
- Year after first system, sold second system for blue/green deployments
- New platform included dedicated compression cards vs CPU compression

### Tactics:
- Problem discovered after data replication showed storage overfill risk
    - we've loaded 30% of the data, but system is 50% full
    - Compression cards reduced efficiency ~40% vs CPUs, leading to undersized system
- Validated compression differences and escalated to engineering
    - Eng., "Yep" 
    - Buried in the OCI, no training, ordering tool not updated, made it past "config check"
    - Still, published, I should have caught, this was my responsibility

### Actions:
- Created Warroom to explored multiple remediation options
    - Remove cards? Can, but IO subsystem is under-plumbed by 15%
    - Increase disk drives?  Lowers CPU/TB, would be very costly
- Arrived at: remove cards, increase system by 15% to compensate for IO (free)
    - removed to keep system simple, no failure risk 

- Delivered custom install: main CPU compression + extra nodes to offset IO shortfall
- Ensured customer satisfaction with tailored solution

### Results:
- Customer received fully functional system with resolved capacity issue
- At no additional cost
- Personal lesson: rigorously review technical documentation for new platforms
- I presented this case on local, regional, and SE all-hands calls
    - try to save others from the same mistake

- Know: Built trust internally and externally through transparency
- Think: Potential tens of millions saved by preventing recurrence

---

# Customer Obsession:
Transparency, accountability, and protecting customers from systemic risk.

- **Ownership** – Took responsibility for mis-sizing, drove resolution and shared lesson broadly.  
- **Customer Obsession** – Ensured customer success by delivering extra nodes at no cost.  
- **Dive Deep** – Validated compression issue through analysis and technical documentation.  
- **Earn Trust** – Built credibility by openly admitting error across teams.  
- **Insist on the Highest Standards** – Resolved to never skim new platform technical documentation again.  
- **Deliver Results** – Delivered working system with custom solution, avoided repeated costly mistakes.  

[Back to the project index page](/projects.html).

---

# Full Text
When I was a SE at Teradata, one of the first customers I covered was a professional social media company with 1.2B users. I had helped them install and onboard their first system, and a year later they wanted to add another identical platform to enable blue/green deployments.  

It was a fairly easy sales cycle, with one caveat: Teradata had upgraded the platform design, adding compression cards to reduce CPU burden and improve cost-efficiency. At first glance this was a value-add, since the customer already used CPU-based compression.  

The problem appeared after replication started—the system was filling too fast, reaching 50% full with only 30% of data loaded. I validated and confirmed with engineers that the compression cards delivered 40% less compression. This undersized the system by 40%.  

Options were considered: CPU-only compression wasn’t viable due to IO limits, larger drives would upset CPU-per-TB balance, and free nodes would be costly. The compromise: disable cards for CPU compression and add 15% nodes free.  

I ensured the customer was satisfied with the fix. Then I openly shared the mistake on SE calls, regional calls, and even all-hands—painful but necessary. If repeated, costs could reach tens of millions. Swallowing pride was worth it. The lesson: never skim technical docs on new platforms, and always prioritize transparency to protect customers.  
