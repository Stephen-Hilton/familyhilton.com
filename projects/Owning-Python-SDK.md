---
- title: "Owning the Python SDK for Customer Experience -- MakeInfinite Labs"  
- description: "Identified immaturity in MakeInfinite Labs’ Python SDK for SXT ZK-Proven DB. Took direct ownership, ensuring usability and quality. Rapidly iterated fixes from customer feedback, republishing improvements. Protected customer experience, raised standards, and delivered most mature, easiest way to interact with API layer."  
- image: "bizstory-generic.png"  
- author: "Stephen Hilton"  
- date: true  
- keywords: "aws loop, projects, learnings"  
- navs: ["top"]  
- highlights:
    - Ownership: Took over the Python SDK directly, ensuring accountability and quality.  
    - Customer Obsession: Focused on usability and rapid fixes to improve customer experience.  
    - Dive Deep: Investigated SDK codebase, uncovered design flaws and non-Pythonic patterns.  
    - Insist on the Highest Standards: Raised bar on SDK usability and design beyond consultant output.  
    - Deliver Results: Delivered rapid iterations, SDK became most mature API interaction path.  
---

# Overview

### Situation:
- MakeInfinite Labs developed SXT ZK Proven DB (Spark, Postgres, Ignite, ZK SQL engine)
- Early customers/prospects struggled with advanced features (e.g., ZK tamperproofing)
- Engineering assigned SDK creation to consultants, but feedback showed immaturity/missing features
- Customer questions exposed usability gaps in Python SDK, espeically with advanced cryptography

### Tactics:
- Started trying to drive consultants to improve, but was time-consuming
- Finally acquired ownership of Github repo, to shifted ownership to SEs
- Goal: Dramatically speed up SDK as critical customer-facing product extension

### Actions:
- Personally reviewed SDK codebase and identified non-Pythonic design
- Took full ownership of Python SDK with SE team backing
- Removed SDK responsibility from consulting team
- Used customer feedback/questions as immediate prompts for SDK improvements
- Pushed back on attempts to return SDK ownership until quality was assured
- Leveraged SDK to work around product limitations, enhancing usability

### Results:
- Python SDK became most mature, simpliest way to access SXT
- Repo has 4k stars and 87 forks, 3rd place 
    - behind only 2 core product repos 
    - ahead of all other SDKs
- Rapid iteration closed customer pain points quickly
- Raised overall quality bar for SDK usability and design
- Improved customer trust and adoption through responsiveness
- Enabled workaround of product limitations via SDK layer

---

# Customer Obsession:
Protecting customer experience and raising SDK quality.

- **Ownership** – Took over the Python SDK directly, ensuring accountability and quality.  
- **Customer Obsession** – Focused on usability and rapid fixes to improve customer experience.  
- **Dive Deep** – Investigated SDK codebase, uncovered design flaws and non-Pythonic patterns.  
- **Insist on the Highest Standards** – Raised bar on SDK usability and design beyond consultant output.  
- **Deliver Results** – Delivered rapid iterations, SDK became most mature API interaction path.  

[Back to the project index page](/projects.html).

---

# Full Text
MakeInfinite Labs is the creator of the SXT ZK Proven DB, which is an amalgamation of Spark, Postgres, Ignite, and a net-new ZK SQL engine, all wrapped in comprehensive APIs. That said, early in the sales cycle, many of our prospects and customers were having challenges using the database, in particular the more complex features like the ZK tamperproofing.

We had several SDKs that a consulting team had generated, which were supposed to make this easier. However, I started hearing feedback, from the broader team but also directly from customers, that the SDK was too immature, or was missing features.

So I did a deep dive on the Python SDK codebase, using a recent customer question/request as the starting point: the confusion of cryptographic keys between user and the table. What I found was that while the SDK was technically working, it was not designed to be easy, nor very Pythonic. Especially for Python, being easy to use is paramount. We needed to have higher standards than what was delivered.

It’s at this point I took over ownership of the Python SDK directly, backed up secondarily by my team, and we removed it from the consultant’s tasks. From that point forward, every time there was a customer question or point of confusion that could be addressed in the SDK, we immediately modified the SDK and republished. In some ways, this wasn’t great, since it meant Solution Engineering now owned a small part of product engineering. However, it delivered extremely rapid results to customers. I insisted on ownership, pushing back on attempts to reclaim control of the SDK until it could be done with real quality for customers. Having SEs own the SDK directly allowed us to work around critical limitations in the core product using the SDK. Even today, the Python SDK is by far the easiest, most mature way to interact with the API layer.
