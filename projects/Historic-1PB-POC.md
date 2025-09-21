--- 
- title: "Historic 1PB POC -- Facebook"  
- description: "Led Teradata’s largest prospect POC: a 1PB data system. Coordinated engineering, sales, delivery, and customer teams. Selected IO-heavy system for complex workloads, hedged with CPU-heavy backup. Ran dual POCs—IO (+70%) and CPU (+700%) — delivering benchmark wins. Lost deal due to late OpenCompute hardware requirement shift. Lessons in pushing for firmer requirements."
- image: "bizstory-generic.png"  
- author: "Stephen Hilton"  
- date: true  
- keywords: "aws loop, projects, learnings"  
- navs: ["top"]  
- highlights: 
    - Ownership: Took accountability for largest POC in company history, aligned resources, drove decision-making.
    - Bias for Action: Made timely system choice despite missing data, mobilized cross-functional teams.  
    - Dive Deep: Analyzed trade-offs (CPU vs IO), led detailed discussions, hedged bets with backup system.  
    - Invent and Simplify: Designed dual-path approach: IO-heavy live POC + CPU-heavy backup.  
    - Earn Trust: Communicated transparently with executives, balanced delivery risks, secured CEO approval.  
    - Deliver Results: Delivered dual POCs, outperforming competitors (+70% and +700%).  
    - Learn and Be Curious: Post-mortem revealed pliability of “hard” requirements, lesson in customer engagement.
---

# Overview

### Situation:
- Largest prospect POC in Teradata history: 1PB data system for world's largest social network ($165B in annual revenue)
- Competing to replace substandard platform
- Coordinated engineering, sales, delivery, and customer exec/data science teams
- Customer provided vague “complex workload” requirement, withheld queries
- Critical design choice: CPU-heavy vs IO-heavy system, high stakes
- Tight timeline, risk of POC delay, CEO-level visibility

### Tactics:
- Structured internal alignment meetings (problem, strategy, recommendation)
- Gained consensus on “pure performance” strategy over price-performance
- Selected IO-heavy system for assumed complexity
- Hedged risk with parallel CPU-heavy prep in Teradata data centers

### Actions:
- Convened engineering, sales, and delivery for problem framing + options
- Reconvened to align on strategy: prioritize absolute performance
- Partnered with engineering + sales to recommend IO-heavy config
- Secured CEO approval despite incomplete requirements
- Built IO-heavy system for deployment
- Prepared CPU-heavy backup, adding modest cost but extending flexibility
- Once queries revealed simple workloads, ran IO POC anyway (+70%)
- Won approval to run CPU-heavy POC in Teradata data center (+700%)
- Delivered dual POCs within a month—unprecedented scale
- Managed customer communication, aligned resources, executed under pressure

### Results:
- Completed largest POC in company history—twice
- IO-heavy POC: beat competitor by +70%
- CPU-heavy POC: beat second place by +700%
- Gained CEO approval and cross-functional alignment
- Ultimately lost deal: added OpenCompute hardware requirements 
- Learned importance of pushing harder on customer requirements, even if “infallible”

---

# Customer Obsession:
High stakes POC, customer-first delivery focus.

- **Ownership** – Took accountability for largest POC in company history, aligned resources, drove decision-making.  
- **Bias for Action** – Made timely system choice despite missing data, mobilized cross-functional teams.  
- **Dive Deep** – Analyzed trade-offs (CPU vs IO), led detailed discussions, hedged bets with backup system.  
- **Invent and Simplify** – Designed dual-path approach: IO-heavy live POC + CPU-heavy backup.  
- **Earn Trust** – Communicated transparently with executives, balanced delivery risks, secured CEO approval.  
- **Deliver Results** – Delivered dual POCs, outperforming competitors (+70% and +700%).  
- **Learn and Be Curious** – Post-mortem revealed pliability of “hard” requirements, lesson in customer engagement.  


[Back to the project index page](/projects.html).

---


# Full Text
I was selected to lead the single largest technical prospect POC in Teradata's history; a 1PB POC data system (spark + relational) to replace a substandard platform at the world's largest social media company (165B annual revenue). I was coordinating engineering resources, sales resources, delivery resources, and customer executives and their data science teams. While the customer had given us a loose requirement of data size and structures, they didn't want to provide "sample user queries" until later, instead simply stating the workload would be "complex." There were several system configurations I could have selected, one cheaper and CPU intensive (good for simple but big workloads) and one more expensive and IO intensive (good for complex / highly concurrent workload). 

I had a limited time to make the choice, so as not to impact the POC schedule. While the customer promised a collection of sample queries, it soon became clear they were not going to deliver prior to our internal date to deploy such a large system. I coordinated a series of internal meetings with engineering, sales, and delivery: the first meeting was to explain the problem (not enough information to properly scope the largest POC in the company’s history) and the three choices we had (CPU heavy, IO heavy, and special cloud instance). Once everyone agreed on the problem and possible choices, we took a break to collect thoughts, and reconvened an hour later for the second meeting: what was the strategy? Compete on absolute performance, or price-performance? Because the customer had said “price is no object,” I gained consensus for “pure performance.” Finally, I led collaboration between Engineering and Sales to arrive at a single recommendation for executive approval: High IO, based on the customer comment, “workload will be analytically complex.” 

That said, because of the size and scale of the POC, I also wanted to hedge our bets; I had the team prepare everything needed to rapidly deploy a CPU heavy system in our own data centers. This added a small additional cost, but extended our deadline another month, if we wanted to change our mind. With that, I had aligned the company behind a decision and ultimately gained CEO approval, despite the lack of several key data elements. 

The results were mixed; once the actual queries were released, the POC was actually NOT analytically complex, but instead very analytically simple, making the workload CPU heavy. Because we had the IO intensive build deployed, we proceeded with the POC as-is and decidedly won the benchmark (by +70%), but I also gained permission (both the customer and internally) to build the CPU heavy system in our own data centers, and re-run the POC there. Within a month we had run the biggest POC in the company’s history twice; once on each platform. The CPU intensive system crushed the POC, delivering +700% better performance than the second-place platform. 

Sadly, the customer changed its requirements in the closing weeks of the POC; they added a requirement to use the OpenCompute standard they had developed, requiring hardware to use 277v rather than 208v (for lower power density, but greater efficiency). This just didn’t work with our high-density designs. 

Do differently? Assuming I couldn’t see the future: I would have gently pushed the customer harder for requirements by the committed dates. I found out later the selected vendor (Vertica, now effectively defunct) pushed back on the 1PB requirement, convincing POC leadership to accept a half-size system, and assume linear scalability (i.e., halve the response time). What the customer presented as infallible requirements were, in fact, more pliable than first thought.

Back to the [project index page](/projects.html).