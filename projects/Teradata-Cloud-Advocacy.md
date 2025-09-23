---
- title: "Advocating Cloud Strategy -- Netflix"  
- description: "As a Solution Engineer embedded at a $40B, 300M-subscriber streaming giant, raised early warnings about cloud migration risk. Advocated cloud strategy despite resistance, delivered stop-gap ‘Teradata Cloud,’ and gave influential keynote urging adoption. Though the customer left, efforts helped push Teradata toward eventual cloud evolution."  
- image: "bizstory-generic.png"  
- author: "Stephen Hilton"  
- date: true  
- keywords: "aws loop, projects, learnings"  
- navs: ["top"]  
- highlights:
    - Ownership: Advocated for Teradata’s cloud adoption despite internal resistance.  
    - Customer Obsession: Elevated customer concerns on cloud migration risk.  
    - Dive Deep: Analyzed customer architecture, gathered competitive insights, sized ‘Teradata Cloud.’  
    - Disagree and Commit: Voiced evidence-centric message, despite pushback from sales leadership.
---

# Overview

### Situation:
- Solution Engineer embedded at global streaming service ($40B revenue, 300M subscribers)
- Customer committed to shutting data centers, moving to cloud (AWS)
- Teradata reliant on high-margin hardware/software model
- Leadership resistant to cloud strategy, cannibalizing revenue
- Redshift not viable but alternatives (Druid, Presto, Athena) emerging

### Tactics:
- Raised cloud risk to sales leadership, marked account “at-risk”
- Started TD Cloud Breakfast Club to advocate for cloud deployments
- Built and shared Redshift competitive materials with Product Marketing

### Actions:
- When customer gave an EOL date for the data center, sales leadership provided: "TD Cloud"
    - Closed “Teradata Cloud” deal (+20% system hosting, billed per-hour)
    - Not real cloud, more "Teradata Hosted", stop-gap at best
- About a year later, delivered keynote at Field Engineering summit on customer cloud ecosystem
    - Delivered evidence-based, dire warning about customer leaving Teradata
    - Ended message as warning to technical community
    - Earned strong support from technical staff, sparking discussion
    - Keynote widely remembered, validated staff concerns, influenced leadership dialogue

### Results:
- After keynote, saw material (if slow) movement towards Cloud
- Less than 12mo later, streaming customer terminated Teradata, moved to Druid/Presto/Athena
- This helped accelerate urgency for cloud strategy “Teradata where you want it”
- Wasn't until Snowflake that Teradata really became "Cloud first", but 5 years too late
    - TD Market Cap: 2B
    - Snowflake Market Cap: 77B (38x)

---

# Customer Obsession:
Listening to customer signals and advocating change.

- **Ownership** – Advocated for Teradata’s cloud adoption despite internal resistance.  
- **Customer Obsession** – Elevated customer concerns on cloud migration risk.  
- **Dive Deep** – Analyzed customer architecture, gathered competitive insights, sized ‘Teradata Cloud.’  
- **Earn Trust** – Voiced evidence-centric message, gaining credibility with technical community.  
- **Disagree and Commit** - Disagree and Commit: Voiced evidence-centric message, despite pushback from sales leadership.

[Back to the project index page](/projects.html).

---

# Full Text
Back when I was a Solution Engineer at Teradata, I spent several years badged at the largest video streaming service company, with over $40B in revenue and 300M subscribers. This customer was a Teradata customer, but also a growing AWS customer rapidly moving into the cloud, aiming to close most owned data centers.  

This was during rapid cloud maturation. AWS had proven massive scalability, and Redshift was emerging. The customer declined Redshift, finding it insufficient for Teradata workloads. My AE and I became convinced Teradata needed a cloud strategy or risk irrelevance. Leadership resisted, preferring hardware margins. We raised concerns, flagged the account “at-risk,” and built Redshift competitive content. Six months later, the customer gave an EOL date, forcing urgency.  

Leadership proposed “Teradata Cloud,” essentially hosted systems billed per-hour, without true elasticity. We closed that multi-million deal, sizing and deploying the system, though recognizing it was stop-gap. Leadership seemed complacent.  

A year later, I presented at Field Engineering summits (Atlanta, Rome) on the streaming customer’s cloud architecture. I closed with a dire warning: this customer would leave without real cloud evolution. While some leaders disliked the message, the technical community embraced it. Dozens thanked me for voicing shared concerns with evidence. For years, people remembered that keynote.  

After the summit, Teradata began shifting narrative to “Teradata where you want it,” though progress was slow. Less than a year later, the streaming giant adopted Druid and Presto (later Athena), terminating Teradata. Urgency increased. With Bay Area SEs, I formed a breakfast club pushing cloud adoption. Snowflake’s rapid rise confirmed the urgency, but by then Teradata was playing defense.  
