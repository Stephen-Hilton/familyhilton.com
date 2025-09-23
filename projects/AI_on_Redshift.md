--- 
- title: "AI on Redshift at Enterprise -- SS&C"  
- description: "Fortune 500 enterprise hesitated to leave AWS Redshift, fearing migration risk. Partnered with Engineering to decouple our AI-SQL engine from data store, creating new product and delivering for the customer. Worked with customer to install, and tested ~90% AI-query accuracy on test data. Won trust, and secured substantial ARR deal."  
- image: "bizstory-generic.png" # image file, as found in /src/images/ folder
- author: "Stephen Hilton" # author of the page, if applicable (should appear in footer)
- date: true # if type date, use as-is.  If "true", use date of last sitegen.py generation.
- keywords: "aws loop, projects, learnings" # SEO / metadata keywords
- navs: ["top"]  # navigation sections that wrap this page. Template for each should be included in /src/templates/navs/[nav].jinja
- highlights: 
    - Ownership: Took accountability for largest POC in company history, aligned resources, drove decision-making.
    - Invent and Simplify:  Built decoupled AI-SQL engine.
    - Earn Trust: Delivered value without forcing migration.
    - Dive Deep: Worked hands-on with engineers + customers to prove accuracy.
    - Deliver Results: Closed mid-6 figure ARR + launched new product offering.
---

# Overview

### Situation: 
- Early prospect of MakeInfinite, Fintech and data firm, $6B/rev and 50k employees
- Wanted AI-SQL Engine to speed up business analytics
- Engaged the team, had a mostly successful sales cycle

### Tactics:
- LT skeptical of migrating off AWS Redshift; trusted AWS uptime over a 1-year-old startup, who knew?  
- As Pragmatic Head of GTM, I felt their objections were not unreasonable

### Actions:
- Gained CEO approval for roadmap change: decouple AI/embedding model from DB-storage
- Partnered with Eng. to come up with a new product! AI-SQL wrapper on any DB
- Given leadership of AI team, decoupled required LLMs:
  - embedding model / RAG
  - SQLCoder for authoring SQL
  - Frontier model to try and catch failures
- Developed training for customer self-maintenance

### Results
- Won deal → became our earliest + longest-running AI customer
- 36k Paid POC + $4k/mo subscription (48k/yr ARR)
- Delivered new product: AI-SQL on top of Redshift!
- Worked with customer AI Eng. to test 90% query accuracy (over-trained?)
- Satisfied customer demand, preserved trust and privacy

---

# Customer Obsession:
Met them where they were (kept Redshift).
- **Invent and Simplify** – Built decoupled AI-SQL engine.
- **Earn Trust** – Delivered value without forcing migration.
- **Dive Deep** – Worked hands-on with engineers + customers to prove accuracy.
- **Deliver Results** – Closed mid-6 figure ARR + launched new product offering.


[Back to the project index page](/projects.html).

---


# Full Text:
MakeInfinte Labs built SXT, an AI data warehouse that understands SQL and Natural Language. Because Microsoft was a big investor in MakeInfinite, we had early access to GPT as far back as GPT3, meaning we had developed products ready for customers when GPT3.5 dropped and really drove AI main-stream. 

As Head of Customer and GTM, I personally oversaw larger enterprise customers and prospects, such as this prospect, who we started working with 18mo ago to purchase our AI-DB. The challenge was: they were perfectly happy with Redshift, and disinclined to endure the effort and cost to migrate their entire data warehouse over to a brand new DB startup, just for this one feature. As a pragmatist/realist and understanding the level of effort required for enterprise scale projects, I complete understood their skepticism. 

We could educate them on all the resiliency / redundancies / uptime features, but at the end of the day, it came down to a risk-assessment; because we’d only been on the market for a year, we didn’t have a decade’s worth of provable up-time data. But they wanted the feature. 

I shifted strategies: working with engineering, we found a low-effort approach to decoupling the AI / embedding model from the DB-storage, allowing us to offer AI-SQL engine on top of Redshift. They could keep their existing, known data platform AND still provide their data analyst (and business leader) community with the ability to ask for new analytics using natural language. It satisfied the customer’s risk tolerance, while still delivering innovative new features; a win-win. We closed the business, and I assigned our top AI engineer to work with SSC directly to (a) build out the first embedding model for their first data subject area, then (b) educate and provide documentation on how they can take over ownership and maintenance for future embedding models / updates. 

They ended up as our earliest and longest-running AI customer. And because we quickly adapted to customer demands, we ended up with a new product; portable AI-SQL engine, deployable on any SQL database.
 