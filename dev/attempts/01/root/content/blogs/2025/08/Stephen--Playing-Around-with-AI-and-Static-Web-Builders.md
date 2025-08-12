I spent a Saturday afternoon building a tiny static webpage builder in Python with the newly released GPT-5. Version one (which you're reading now) is admittedly kind of ugly, but it also came together in just a few hours, and that’s the whole point: fast, clear progress beats perfect polish when you’re learning and shipping.

After struggling thru the weirdness that was Jekyll and running into problem after problem, I decided - forget this, I'm going to see if GPT-5 can auto-generate a similar static webpage builder in less time than I burned floundering around Jekyll (spoiler: it can, but doesn't look as good). The concept was simple: read content from YAML/Markdown, run it through Jinja templates, and spit out clean HTML into a root/ folder you can serve with python -m http.server or upload to a github page. 

I started by writing a requirements document, getting the bare-bones on paper (er, digitally speaking) and having GPT-5 help me flesh out details and provide recommendations.  Once I was happy with the requirements, **but before I submitted for code generation** I asked GPT-5 what questions it had about the document... and it had many, eroding my previous happy-state.  After another 45mins of extending the document, I felt it was good enough to get started!

I asked GPT-5 to sketch the skeleton: a sitegen package with build, clean, and init commands; a templates/ directory for base.html, home.html, blog_index.html, etc.; and a content/ directory where index.yaml, blogs.yaml, and people.yaml live alongside subfolders full of .md files. From there, it was a steady back-and-forth: I described how I wanted blog posts parsed (author and title from the filename), how the homepage hero should read CTAs, and how images in Markdown should resolve from a shared _images folder. GPT-5 handled the boilerplate fast.

The first execution of the code had 1 error, and I had a copy/paste error (AI:1, human:1, tied game).  But after a little adjustment we were in business: index.html appeared, pages/blogs.html listed posts, and individual blog and people pages rendered from Markdown with a minimal header and footer.  We even got extras like sitemap.xml and robots.txt for free. 

Was it pretty? Not yet. The initial CSS looked like it had been borrowed from 2008, and the nav links huddled together like a single long word. But that’s the magic of a quick prototype—you can see the whole loop: schema → template → output. Now the improvements are obvious.

Is this production-ready? Not yet. But in a couple hours, I went from nothing to a custom static generator I understand end-to-end. I also have learnings on how I'll structure the v2 (a project for a future Saturday): I'll likely get more prescriptive on the yaml, collapse many of the custom section types into fewer, more flexible options, and layer in more assumptions to comb out complexity. This is for simple, static, family type websites.   After that, I'm thinking MCP server!

For now, I’m calling it a win. The first attempt may be ugly, but I did generate it faster than struggling with Jekyll.  
Let me know what you think:

https://github.com/Stephen-Hilton/familyhilton.com