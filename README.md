# Static Site Generator

A Python-based static site generator that converts YAML configuration files and Markdown content into a complete static website.  It's dynamic, simply iterating over the contents of the project root directory, and picking up / converting all content it finds.

For an example, see my simple family page:  https://familyhilton.com  which is running directly from this repo.

## Quick Start:

This guide assumes you know the basics of yaml and markdown.  No worries if they're new to you, both are very easy - check out these tutorials on [yaml](https://spacelift.io/blog/yaml) and [markdown](https://www.markdowntutorial.com/).

To get started building your own webpage: 

1. Create / login to your [Github.com](https://githublcom) account
2. Fork the FamilyHilton.com repo and rename to something meaningful to you:<br>
[https://github.com/Stephen-Hilton/familyhilton.com/fork](https://github.com/Stephen-Hilton/familyhilton.com/fork)
3. Clone your new repo locally by opening a terminal window on your computer and enter:<br>`git clone https://github.com/<your-name>/<your-repo-name>.git`
4. Install the builder and dependencies (-i), build your site, and open in a local webserver for testing (-w), all by typing in your terminal window:<br>
  `. ./src/build_site.sh -i -w`

Done!  You should now have a local copy of https://familyhilton.com running locally (as something close to http://localhost:8000).  

Time to make it your own... try these steps:

**- Add your own "PERSON" page:**
  - Open up the "people" directory, copy/paste "stephen.md" and rename to "your_name.md"
  - Open your new .md file and update the config information, then save
  - When done, run `/src/build_site.sh` to rebuild the site
  - Refresh your browser window to see changes
  - Click on on the "People" navigation, you should see your new page!
  - Remove Stephen, Joy, etc. and start filling in your own folks.
  - Try the same with pets, blogs, etc.

**- Add a new "Core" page**
  - In the project root directory, copy/paste the `/about.yaml` and rename, let's say `/popcorn.yaml`
  - Open your new .yaml file and update the config information, then save
  - When done, run `/src/build_site.sh` to rebuild the site
  - Refresh your browser window to see changes
  - You should see a new "Popcorn" page available on all nav sections!
  - Try the same again, this time copy/pasting `/pets/luna.md` to the root directory, and renaming to `/soda.md` and updating the configuration. 
 
If you don't want to see "Popcorn" on navs, or you want the nav pages in a different order, you can explicitly define in the `/index.yaml` under the `site` section, `nav_pages` value, which is a list of pages, in display order.

**- Push to Github and Setup Hosting**
  - Commit your changes to Github, by entering in your terminal window:<br>
  ```shell
  git add .
  git 
  ```


- You can host on github pages directly, or via AWS S3 static pages.  See details at the bottom of this page.

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

## Create Your Config Files
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
    ├── build_site.sh       # Install, build site, start webserver (-w)
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

For example, you might have a subfolder called `/blogs/` in which you write and store many blog files as markdown.  You then create a `/blogs.yaml` page that includes a section `type: pagelist.tiles` which points to your `/blogs/*` subfolder.  When build_site.sh is executed, it will turn all .yaml and .md files into html, generate a section in the newly created `/blogs.html` that iterates and display a listing of all pages in the subfolder `/blogs/*.html`.  

Another example, the `/people.yaml` config contains a section for `type: pagelist.cards` that points at your subfolder `/people/*.md`.  When build_site.sh is executed, it generates the `/people.html` page, which lists all people and links their personal pages stored in `/people/*.html`.   

Both of the above examples can be found in this repo. 

### [image].png (and other image types)
All images are expected to exist in the /src/images/* folder, so any configuration that specifies an image file, assume that image is stored in the /src/images/* folder.  For example, `image: "logo.png"` would actually be located at `image: "/src/images/logo.png"`.  These can be any web-safe image type (including video), and are here to be referenced by various pages. 

## Config Files You'll Probably NOT Care About:
Unless of course you're a webdev, in which case, please contribute!

### python (sitegen.py)
This is the main python engine that, when executed via `python3 ./src/sitegen.py` will build all html pages as specified above.  This is typically called with the wrapper script, `. ./src/build_site.sh` which also builds the python virtual machine, installs all dependencies, and optionally (-w) starts a local webserver. 

### [sectiontype].jinja
When adding sections to your page.yaml file, each section must map to a .jinja file found in `/src/templates/sections/`.  

Each jinja template can have unique variable requirements, which should be documented (in comments) at the top of the jinja file.  A few common examples include title, description, image, author, date, keywords, markdown content, etc.  Some more advanced pages, such as a "pagelist.cards" template may also require variables such as pagination details, sorting direction, subfolder to iterate, filters, etc.

If you're starting a new yaml section, you should be able to copy/paste the complete config dict from the example in the jinja file.  If you want to extend the section types, make sure the `type: section_name` has a corresponding jinja file in `/src/templates/sections/section_name.jinja`.  This makes the framework very easy to extend -- then make sure to add a PR so others can enjoy!

BTW, jinja files should not contain css or js, but rather reference the site-wide style found in `/src/cssjs/default.css` and `/src/cssjs/default.js`.   

As with any file in the /src/ subdirectory, these files should not change frequently.

### [theme].css and [theme].js
The css and javascript files are all expected to be stored in the /src/cssjs/ folder.  Because there may be global or special-use css and js files, the /index.yaml file contains a "site/"themes" section that defines theme names and assigns the css and js files explicitly, however always assumes the files exist in /src/cssjs subfolder. 

**NOT YET IMPLEMENTED** - currently, dynamic theme switching hasn't been added to the framework.  Not hard, just not a priority at the moment.  Feel free to extend and open a PR!  Just remember, it has to be done 100% client-side.

As with any file in the /src/ subdirectory, these files should not change frequently.


## Generating the Site

Once you've set your config files, it's time to compile them into html files, aka your working webpage!  

### First Run?
If this is the **first time running the script**, open a terminal window and:
```bash
. ./src/build_site.sh -i -w
```

### Generating Site
To synthesize all config files into html and build your site, use the command:

```bash
. ./src/build_site.sh
```
**Available flags:**
- `-i` - Install/update Python dependencies (required on first run)
- `-w` - Start local webserver for testing (blocking terminal, `ctl-C` to quit)


The `build_site.sh` script will:
1. Convert all `.yaml` or `.md` files in the root directory to HTML
2. Convert `.md` files in subdirectories to HTML
3. Create a timestamped log file in `src/logs/`

Optionally perform install/upgrade and start a webserver.

**Examples:**
```bash
. ./src/build_site.sh -i -w    # First run with webserver
. ./src/build_site.sh -w       # Generate site and start webserver
. ./src/build_site.sh -i       # Update libraries and generate site
. ./src/build_site.sh          # Just generate site
```


# Hosting

The generated HTML files can be hosted on:
- GitHub Pages
- AWS S3 Static Website Hosting
- Netlify
- Vercel
- Any static web server

I'll try to add instructions on how to set up at various places shortly. 

## Dependencies
All dependencies are installed and kept up-to-date automatically by the `./src/build_site.sh` script.

- Python 3.6+
- PyYAML
- Jinja2
- Markdown
- python-dotenv

Dependencies are automatically installed when running the generator (-i).

## Logs

All generation activity is logged to timestamped files in `src/logs/` for debugging and monitoring.



# Does the world need another static-webpage builder?  

Probably not, but those that I found today were overly complicated for my super-simple use-case; a family webpage.  Specifically, I wanted something that was:
- static, to be hosted on github pages or S3 bucket
- simple, close to zero-code so all family members can edit (just markdown)
- able to host free, or nearly free
- decent looking but MORE importantly, dead-simple to update
- easy to extend / add new pages quickly
- did I mention: simple?


Jekyl was cool, but way more complex than I needed, and too much education required for the family. It felt like hunting squirrels with a bazooka.  I am willing to sacrifice a lot of flexibility for simplicity, at least for this project.

Also, it was fun. It was a chance to exercise AWS-Q with Claude 4.0 LLM - yes, obviously most of this was vibe coded. It took me several hours to architect how I wanted it to work and build out my desired structures for yaml and markdown by hand, and about 10 minutes for Q to create the entire working application with about 80% accuracy, then maybe another few hours of prompting for various fixes and updates to arrive at what you see here. It's not prefect yet, but for a little family site that's easy to stand up on github pages, I'm declaring victory and moving on for now. 

So... no, I probably didn't need to do this. But it was a fun little side project, no apologies. 

## Open to Contributions
When I was wrapping up initial dev, I prompted Claude to:

>Please generate a comprehensive context compression summary, saved to a file `/src/ai_context.md` as a markdown format.  Design it to be optimal for the below future prompt:
> 
>Please read the file /src/ai_context.md to understand the project goals and context history before the next request.

That way, if you want to vibe code new features / functionalities, you have a handy context file to start with. If you are on AWS Q (as with many tools) it'll just read the entire project, including that context file. 