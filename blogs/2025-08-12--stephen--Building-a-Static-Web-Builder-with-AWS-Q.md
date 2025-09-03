--- 
  - title: "Building a Static Web Builder with AWS-Q (for Github Pages)"  # title of the page, also the browser tab title
  - description: "For small projects, vibe coding a new static web framework is officially faster than just reading the docs of existing frameworks."  # description / subtitle
  - image: "2025-08-12--stephen--Building-a-Static-Web-Builder-with-AWS-Q.png" # image file, as found in /src/images/ folder
  - author: "Stephen Hilton" # author of the page, if applicable (should appear in footer)
  - date: 2025-08-12 # if type date, use as-is.  If "true", use date of last sitegen.py generation.
  - keywords: "family, blog, updates, projects, adventures" # SEO / metadata keywords
  - navs: ["top"]  # navigation sections that wrap this page. Template for each should be included in /src/templates/navs/[nav].jinja
---


I spent a Saturday afternoon building a small static webpage builder in Python with the new AWS-Q extension for VSCode. Version one (which you're reading now) could admittedly use some tweaking, but it also came together in a few hours, and that’s the whole point: fast, iterative progress over perfect while you’re still experimenting.  With AI it's never been easier. 

## Requirement 

This started after I decided to update our aged [https://familyhilton.com](https://familyhilton.com) family website.  It was previously on Wix.com just as a convenience. We rarely updated the content, and $10/mo hosting seemed like overkill for such a simple site. For the amount of traffic we get, Github Pages would work just fine, and - even better - for free.

## Why Build New?

I always start any problem with looking for an easy, existing solution.  Github Pages is tightly integrated with the Ruby framework Jekyll, so I started there, hoping that 30 minutes of playing / learning would result in a working site.  Cut to several hours later and me still struggling with the weirdness of Jekyll, running into problem after problem. I finally took a break to reset, and ask the question, "I just want a super-simple static webpage, why is this so hard?  How would I re-architect for simplicity?"  If I was going to spend the time, I'd rather try out AWS-Q and see if I can auto-generate a similar static webpage builder in less time" (spoiler: yes I can, but admittedly doesn't look as good). 

## The Concept

The concept was simple: read content from YAML/Markdown, run it through Jinja templating engine in Python, and spit out clean HTML into a root/ folder as a static web page served in platforms like Github pages or AWS S3. Make the process primarily file-base, error-resistant, and easy enough for almost anyone to operate - it is a family website, so anyone in the family needs to operate.

## The Requirements

I started with a requirements document, which was going to be my prompt. I spent time getting the bare-bones on paper (er, digitally speaking) and having AWS-Q (using Claude Sonnet) help me flesh out details and provide recommendations.  Once I was happy with the requirements, **but before I submitted for code generation** I asked AWS-Q what questions it had about the document... and it had many, eroding my previous happy-state.  After another 45mins of extending the document, I felt that my requirements doc (aka prompt.md) was good enough to submit.

The final requirements: a single sitegen.py script with methods to build, test, and even serve (using local https server) a static website using a series of simple config files.  Config files would live in the project root, to make it easy to move to Github Pages or AWS S3 hosts, and to keep it dead-simple for non-technical users to modify (same reason I went with yaml instead of json).  Each config file would produce an identically named html file (e.g., index.yaml produced index.html, blogs.yaml produced blogs.html, etc.), with dynamic sections that allowed the engine to iterate through subfolders and produce N-number of subpages (e.g., blogs.html included an index for `/blogs/*.md`). Basically, the MVP for what a "family" website might want: a home page, an about page, and index pages for N-number of blogs, people, and pet pages, all neatly indexed.  Easy, but extensible - new pages were just a new yaml file.

Any technical files were tucked into a `/src/` subfolder, including the python engine, jinja templates, css / js, etc.  This was to declutter the content for the non-technical user. 

## The Build

After about 2 hours of fiddling with requirements and yaml config design, I fired off my fairly verbose prompt.md to AWS-Q, and within about 10 minutes had all code built. The first execution of the sitegen.py had 1 error, which was easily handed to AWS-Q and fixed. The website then built incorrectly, which was a human copy/paste error (AI:1, human:1, tied game).  With those adjustment made we had a working site!  index.html appeared, pages/blogs.html listed posts, and individual blog and people pages rendered from Markdown with a minimal header and footer.

Was it pretty?  Meh, let's say 6/10.  The initial CSS generated by AWS-Q looked like it had been borrowed from 2015, and the nav link hover-overs are a weird yellow, but those are both just tastes, not broken - and only a prompt-fix away.  But more importantly, that’s the magic of a quick prototype — you can see the whole project in miniature, all at once: requirements → context → llm codegen → product test → repeat.  Now the improvements needed are real and obvious, not hidden in a theoretical state, weeks to discovery.

## Next Steps

This was for a small family site, so... honestly not much left to do.  I may go back and fix some of the colors, either prompting or with simple CSS edits.  But perfection was never the point - in just a couple hours, I went from nothing to a custom static webpage generator, built to my bespoke requirements (90% of that time was defining the requirements). I can easily see the changes needed for v2 (a project for a future Saturday, maybe): I'll likely expand color configs into the yaml, collapse many of the custom section types into fewer, more flexible options, and layer in more assumptions to comb out complexity. This is for simple, static, family type websites, so simple is better.   After that, I'm thinking MCP server!

This was initially deployed on Github pages, but with very little effort (and some help from AWS-Q in the AWS console) I was able to stand up the same static site on AWS in about 15 minutes.  A more immediate next-step: setup a CI/CD pipeline to auto-sync S3 after a Github.com merge. 

For today, I’m calling it a win and moving on.  Let me know what you think:

- [familyhilton.com](https://familyhilton.com) (Github Pages - this is the "real" site)
- [hilton.zone](http://hilton.zone) (AWS S3 / Route 53 -- http only, not https. Just for testing!)
- [github.com/Stephen-Hilton/familyhilton.com](https://github.com/Stephen-Hilton/familyhilton.com) (code)

## Epilogue

The oversimplification that "SaaS is Dead" has been repeatedly refuted.  Rather, the "SaaS Hayday is Done."  i.e., SaaS will continue, but not likely spawning new megaliths like SalesForce.com or Twilio, especially when those products still come with guaranteed uptime.  Enterprises will pay a premium to hand the worry and cost of support to a 3rd party, and who better than the authors of the service?

But - the Hayday is done.  Remember, I used wix.com until recently.  In 2 hours I created a novel, bespoke web framework for a target audience using AI, which effectively replaced my need for the Wix SaaS.  Why?  Because I was using Wix as a hosting platform with a page builder simple enough that my family could manage edits.  Wix's product was just a product to me - one easily replaced with AI, given my very simple requirements.

The SaaS providers who survive are right now scrambling to re-focus on the experience and outcome, not the product.  Lovable figured that out, which is why there are now hundreds of Lovable clones. 

Maybe another way to say it: "SaaS is Becoming a Commodity", aka increasingly undifferentiated, unless they can adapt to the coming AI world.  
