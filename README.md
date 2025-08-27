# Static Site Generator

A Python-based static site generator that converts YAML configuration files and Markdown content into a complete static website.  It's dynamic, simply iterating over the contents of the project root directory, and picking up / converting all content it finds.

For an example, see my simple family page:  https://familyhilton.com

To use: 
1. Modify / add / remove .yaml config files in the project root, one yaml per webpage.
2. Modify / add / remove .md config files from subfolders, such as `/blogs/*.md`
2. Execute the `/src/sitegen.py` script to transform config files in html webpages.
3. Optionally, execute `/src/webserver_start.py` to launch a local webserver and test your page.


# Does the world need another static-webpage builder?  

Probably not, but those that I found today were overly complicated for my super-simple use-case; a family webpage.  Specifically, I wanted something that was:
- static, to be hosted on github pages or S3 bucket
- able to host free, or nearly free
- decent looking but dead-simple to maintain
- easy to extend / add new pages quickly
- zero-code so all family members can edit (just markdown)

Jekyl was cool, but way more complex than I needed, and too much education required for the family. I felt like I was hunting squirrels with a bazooka. 

It was also a chance for me to exercise AWS-Q with Claude 4.0 LLM - yes, obviously most of this was vibe coded. It took me several hours to architect how I wanted it to work and build out my desired structures for yaml and markdown by hand, and about 10 minutes for Q to create the entire working application with about 80% accuracy, then maybe another few hours of prompting for various fixes and updates to arrive at what you see here. It's not prefect yet, but for a little family site that's easy to stand up on github pages, I'm declaring victory and moving on for now. 

So... no, I probably didn't need to do this. But it was a fun little side project.  

## Open to Contributions
When I was wrapping up initial dev, I prompted Claude to:


>Please generate a comprehensive context compression summary, saved to a file `/src/ai_context.md` as a markdown format.  Design it to be optimal for the below future prompt:
> 
>Please read the file /src/ai_context.md to understand the project goals and context history before the next request.

That way, if you want to vibe code new features / functionalities, you have a handy context file to start with. If you are on AWS Q (as with many tools) it'll just read the entire project, including that context file. 


# Features

- **YAML Configuration**: Define page structure and content using YAML files
- **Markdown Support**: Write content in Markdown with YAML frontmatter
- **Jinja2 Templates**: Flexible templating system for layouts and components
- **Multiple Themes**: Built-in support for default, light, and dark themes
- **Responsive Design**: Modern, mobile-friendly CSS and JavaScript
- **Interactive Elements**: Smooth animations, navigation, and user interactions
- **Blog Support**: Automatic blog post listing and sorting
- **Static Output**: Generates pure HTML/CSS/JS for hosting anywhere

# Usage
There is no UI for this project - instead, it is all file-driven.  To create a new webpage, simply create a new yaml file, configure what settings and sections you want, save, and re-run `/src/sitegen.py` to rebuild the static website.

## Types of Config Files
There are several types of config files, each used for a specific purpose.  Some are used to build the site and will change frequently, some are more back-end and will change infrequently - and only if you understand things like CSS and JS (or can ask AI to update).

### Sample File Structure

```
root/
├── index.yaml              # Homepage configuration
├── about.yaml              # About page configuration
├── blogs.yaml              # List of Blog posts
├── blogs/                  # Folder for individual blogs
│   └── *.md                # Markdown blog posts
├── people.yaml             # List of People profiles
├── people/                 # Folder for individual profiles
│   └── *.md                # Markdown people profiles
└── src/                    # Source files (modify with care / infrequently)
    ├── sitegen.py          # Main generator script
    ├── webserver_start.py  # local webserver for testing
    ├── logs/               # location of sitegen logs
    ├── cssjs/              # CSS and JavaScript themes
    ├── images/             # Site images
    ├── icons/              # UI icons
    └── templates/          # Jinja2 templates
        ├── navs/           # Navigation templates
        └── sections/       # Content section templates
```

## Config Files You'll Probably Care About:

### [page].yaml
Highest level file, containing configuration details on how to build the final html file.  The output html filename will be the same name as the yaml filename and in the same folder (but with a different extension). The yaml file contains a "page" dict (config section) defining all settings for the html page, such as title, logo, keywords for SEO, and navigation divs.  Below the "page" dict is a "sections" list, which has N-number of sections defined.  Each "section" in the yaml "sections" is a new part of the html body to be appended to the end, so that the final html page mirrors the order in which the sections appear in the yaml.  The "secion" "type" needs to map to one of the .jinja files in `/src/templates/sections/[type].jinja`.  See the section on .jinja below for how to add new section types.

Currently available sections include:
- **hero**: a "hero" section appropriate for landing page, along with call-to-action buttons
- **markdown**: a generic section containing arbitrary markdown
- **divider**: a simple horizontal line (HR) for breaking up sections
- **features**: a list of elements (for example, features of a product)
- **pagelist.cards**: iterate over a subdirectory and display one large 'card' per subpage found
- **pagelist.tiles**: iterate over a subdirectory and display one medium 'tile' per subpage found

An example yaml file might look like:

```yaml
page:
  title: "My Page Title"  
  description: "Some description for your page." 
  image: "logo.png" 
  author: "your name"
  date: true  # if type date, use as-is.  If "true", use date of last sitegen.py generation.
  keywords: "family, blog, updates, projects, adventures" # SEO / metadata keywords
  navs: ["top", "footer", "left"] 

sections:
  - type: "hero"
    title: "Welcome"
    subtitle: "Site subtitle"
    hero_image: "banner.png"
    
  - type: "markdown"
    heading: "Content"
    content: |
      Your **markdown** content here.
```

Note, index.yaml contains one extra section, "site", which allows configuration of site-level attributes, such as favicon, title, SEO, etc. 

### [page].md
Along with yaml, markdown files can also be generated into html files by the python engine.  As with yaml, the html page created shares a name and folder location with the markdown file, so /people/stephen.md would be used to create /people/stephen.html.  The markdown file will contain a "yaml front matter" header fenced in "---" delimiters, that contains ths same keys as the yaml "page" dict.  Unlike the yaml file, the markdown file does not have any "section" list - instead, the rest of the markdown content of the file is translated to HTML and used as the entire body of the page.

In other words, using a markdown file is the same as using a yaml file with one section of `type: "markdown"`, except as a markdown file, you can use wysiwyg editors.

If there is both a yaml and markdown file that share a name (i.e., /people/stephen.yaml and /people/stephen.md), the yaml file is used, ignoring the .md file.

An example markdown file might look like: 
```markdown
---
- title: "Page Title"
- description: "Page description"
- author: "Author Name"
- date: 2025-01-01
---

Write your content in **markdown** here.  Could be a blog post or some other arbitrary content. 

Have fun and explore!
```

The typical use-case for Markdown is to keep longer user-generated content stored in a sub-directory, such as blog posts or people's bios.  A common practice will be to generate one yaml file that displays many subpages, all generated and stored in a subfolder. 

For example, you might have a subfolder called `/blogs/` in which you write and store many blog files as markdown.  You then create a `/blogs.yaml` page that includes a section `type: pagelist.tiles` which points to your `/blogs/*` subfolder.  When sitegen.py is executed, it will turn all .yaml and .md files into html, generate a section in the newly created `/blogs.html` that iterates and display a listing of all pages in the subfolder `/blogs/*.html`.  

Another example, the `/people.yaml` config contains a section for `type: pagelist.cards` that points at your subfolder `/people/*.md`.  When sitegen.py is executed, it generates the `/people.html` page, which lists all people and links their personal pages stored in `/people/*.html`.   

Both of the above examples can be found in this repo. 

### [image].png (and other image types)
All images are expected to exist in the /src/images/* folder, so any configuration that specifies an image file, assume that image is stored in the /src/images/* folder.  For example, `image: "logo.png"` would actually be located at `image: "/src/images/logo.png"`.  These can be any web-safe image type (including video), and are here to be referenced by various pages. 

### python (sitegen.py and webserver_start.py)
This is the main python engine that, when executed via `python3 ./src/sitegen.py` will build all html pages as specified above.  

Additionally, test your changes locally by executing via terminal: `python3 ./src/webserver_start.py` which will start a local webserver and open your page. 

## Config Files You'll Probably NOT Care About:
Unless of course you're a webdev, in which case, please contribute!

### [sectiontype].jinja
When adding sections to your page.yaml file, each section must map to a .jinja file found in `/src/templates/sections/`.  

Each jinja template can have unique variable requirements, which should be documented (in comments) at the top of the jinja file.  A few common examples include title, description, image, author, date, keywords, markdown content, etc.  Some more advanced pages, such as a "pagelist.cards" template may also require variables such as pagination details, sorting direction, subfolder to iterate, filters, etc.

If you're starting a new yaml section, you should be able to copy/paste the complete config dict from the example in the jinja file.  If you want to extend the section types, make sure the `type: section_name` has a corresponding jinja file in `/src/templates/sections/section_name.jinja`.  This makes the framework very easy to extend -- then make sure to add a PR so others can enjoy!

BTW, jinja files should not contain css or js, but rather reference the site-wide style found in `/src/cssjs/default.css` and `/src/cssjs/default.js`.   

As with any file in the /src/ subdirectory, these files should not change frequently.

### [theme].css and [theme].js
The css and javascript files are all expected to be stored in the /src/cssjs/ folder.  Because there may be global or special-use css and js files, the /index.yaml file contains a "site/"themes" section that defines theme names and assigns the css and js files explicitly, however always assumes the files exist in /src/cssjs subfolder. 

**NOT YET IMPLEMENTED** - currently, dynamic theme switching hasn't been added to the framework.  Not hard, just not a priority at the moment.  Feel free to extend and open a PR!

As with any file in the /src/ subdirectory, these files should not change frequently.





## Usage

### Generate the Site

```bash
python3 src/sitegen.py
```

This will:
1. Process all `.yaml` files in the root directory
2. Convert `.md` files to HTML (if no corresponding `.yaml` exists)
3. Create a timestamped log file in `src/logs/`



### Hosting

The generated HTML files can be hosted on:
- GitHub Pages
- AWS S3 Static Website Hosting
- Netlify
- Vercel
- Any static web server

I'll try to add instructions on how to set up at various places shortly. 

## Dependencies

- Python 3.6+
- PyYAML
- Jinja2
- Markdown

Dependencies are automatically installed when running the generator.

## Logs

All generation activity is logged to timestamped files in `src/logs/` for debugging and monitoring.