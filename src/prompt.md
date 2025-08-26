# Prompt Summary
Please create a python engine called "sitegen.py" that, when executed, traverses a supplied folder, reads in various configuration files, and produces a static webpage that can be hosted using methods like github pages or S3 static pages.

# Folder Structure Example
Below is an example file/folder structure *before the python engine executes* (aka config files).  The actual files and folders may vary, depending on use:
 

```text
root/
├── index.yaml
├── about.yaml
├── links.yaml
├── blogs.yaml
├── blogs/
│   ├── 2025-08-01--stephen--Confessions-of-GenX-Tech-Leader.md
│   └── 2025-08-12--stephen--Vibe-Coding-Web-Builder.md
├── people.yaml
├── people/
│   ├── Stephen.md
│   ├── Joy.md
│   ├── Tate.md
│   └── Quinn.md
├── pets.yaml
├── pets/
│   ├── Luna.md
│   ├── Sunny.md
│   └── Zelda.md
└── src/
    ├── sitegen.py (engine)
    ├── cssjs/
    │   ├── default.css
    │   ├── default.js
    │   ├── light.css
    │   ├── light.js
    │   ├── dark.css
    │   └── dark.js
    ├── icons/
    │   ├── user.svg
    │   ├── phone.svg
    │   └── pet.png
    ├── images/
    │   ├── logo.png
    │   ├── favicon.png
    │   ├── stephen.png
    │   ├── joy.png
    │   ├── tate.png
    │   ├── quinn.png
    │   ├── luna.png
    │   ├── sunny.png
    │   └── zelda.png
    └── templates/
        ├── navs/
        │   ├── top.jinja
        │   ├── left.jinja
        │   ├── right.jinja
        │   └── footer.jinja
        └── sections/
            ├── divider.jinja
            ├── gallery.jinja
            ├── hero.jinja
            ├── markdown.jinja
            ├── pagelist.cards.jinja
            ├── pagelist.table.jinja
            ├── pagelist.tiles.jinja
            └── map.jinja
```

# Types of Config Files:
There are several types of config files, each used for a specific purpose:

### [page].yaml
Highest level file, containing configuration details on how to build the final html file.  The output html file should be the same name as the yaml file and in the same folder (but with a different extension). The file contains a "page" yaml dict outlining html page leve configuration, such as title, logo, keywords for SEO, and navigation divs.  Below the "page" dict is a "sections" yaml list, which has N-number of sections defined as yaml dicts.  Each "section" in the yaml "sections" is a new part of the html body to be appended to the end, so that the final html page mirrors the order in which the sections appear in the yaml.  The "secion" "type" needs to map to one of the .jinja files in "/src/templates/sections/[type].jinja".  For example, the /about.yaml file contains one section with the type "markdown".  The engine will create a new file /about.html with the page characteristics found in the /about.yaml "page" dict, with one page body section built from the html tempate found in /src/templates/sections/markdown.jinja, and the content found in the /about.yaml as defined in the "markdown" section.  

### [page].md
Along with yaml, markdown files can also be generated into html files by the python engine.  As with yaml, the html page created shares a name and folder location with the markdown file, so /people/stephen.md would be used to create /people/stephen.html.  The markdown file will contain a "yaml front matter" header fenced in "---" delimiters, that contains ths same keys as the yaml "page" dict.  Unlike the yaml file, the markdown file does not have any "section" list - instead, the rest of the markdown content of the file should be fed into the "/src/templates/sections/markdown.jinja" template for html file generation. 

In other words, the markdown file is the same as a yaml file with one section of `type: "markdown"`. 

If there is both a yaml and markdown file that share a name (i.e., /people/stephen.yaml and /people/stephen.md), use the yaml file and ignore the .md file.

The typical use-case for Markdown is to keep longer user-generated content, such as blog posts or people's bios.  A common practice will be to generate one yaml file that displays many subpages, all generated and stored in a subfolder. For example, there may be a /blogs.yaml page that generates a /blog.html, which displays a listing of all pages in the subfolder /blogs/*.html.  Each of the /blogs/*.html were genereated from matching /blogs/*.md files.

Another example, the /people.yaml is used to generate the /people.html page, which lists all people and links their personal pages. People's personal pages all reside in the subfolder /people/*.md, which the engine turns into /people/*.html, using the "yaml front matter" definition for the page configuration, and the /src/templates/sections/markdown.jinja template. 
 
### [sectiontype].jinja
This is the template html section, the content to be used from the /[page].yaml definition above and inserted into the final /page.html output.  This should not contain css or js, but rather reference the site-wide style found in /src/cssjs/default.css and /src/cssjs/default.js.  A "theme" would be the combination of this /src/cssjs/theme_name.[css|js]. 

Some jinja are designed to iterate over many files in a subfolder, and display a list.  For example, /blogs.yaml has a section type defined as "pagelist.cards" which should map to /src/templates/sections/pagelist.cards.jinja.   This template should generate one card per blog file found under /blogs/*.md.  

Each jinja template can have unique variable requirements, which should be documented (in comments) at the top of the jinja file.  A few common examples include title, description, image, author, date, keywords, markdown content, etc.  Some more advanced pages, such as a "pagelist.cards" template may also require variables such as pagination details, sorting direction, subfolder to iterate, filters, etc.

As with any file in the /src/ subdirectory, these files should not change frequently.

### [theme].css and [theme].js
The css and javascript files are all expected to be stored in the /src/cssjs/ folder.  Because there may be global or special-use css and js files, the /index.yaml file contains a "site/"themes" section that defines theme names and assigns the css and js files explicitly, however always assumes the files exist in /src/cssjs subfolder. As with any file in the /src/ subdirectory, these files should not change frequently.

### [image].png (and other image types)
All images are expected to exist in the /src/images/* folder, so any configuration that specifies an image file, assume that image is stored in the /src/images/* folder.  For example, `image: "logo.png"` would actually be located at `image: "/src/images/logo.png"`.  These can be any web-safe image type (including video), and are here to be referenced by various pages. 

### python (sitegen.py)
This is the main python engine that, when executed via `python3 ./src/sitegen.py` will build all html pages as specified above.  If this script gets too long, or there is a desire to break the file into smaller, more easily managed peices, a /src/sitegen/* folder can be created and used.   This is the ONLY exectuable file in the project.

# Site Level Config
There are a few site-wide configurations, such as favicon or site name.   These can be found in the "/index.yaml" page, under the yaml "site" dict.  

# Expected Outcome
Given the content above, once the user locally executes `python3 ./src/sitegen.py` the engine should combine all filetypes as defined above, resulting in the below file/folder structures.

Note, all the config files remain untouched, however the process has now added appropriate html files to mirror any .[page].yaml and page.md files.  Also note that nothing under the /src/ folder is changed, since that is entirely config files. 

```text
root/
├── index.yaml
├── index.html
├── about.yaml
├── about.html
├── links.yaml
├── links.html
├── blogs.yaml
├── blogs.html
├── blogs/
│   ├── 2025-08-01--stephen--Confessions-of-GenX-Tech-Leader.md
│   ├── 2025-08-01--stephen--Confessions-of-GenX-Tech-Leader.html
│   ├── 2025-08-12--stephen--Vibe-Coding-Web-Builder.md
│   └── 2025-08-12--stephen--Vibe-Coding-Web-Builder.html
├── people.yaml
├── people/
│   ├── Stephen.md
│   ├── Stephen.html
│   ├── Joy.md
│   ├── Joy.html
│   ├── Tate.md
│   ├── Tate.html
│   ├── Quinn.md
│   └── Quinn.html
├── pets.yaml
├── pets/
│   ├── Luna.md
│   ├── Luna.html
│   ├── Sunny.md
│   ├── Sunny.html
│   ├── Zelda.md
│   └── Zelda.html
└── src/
    ├── sitegen.py (engine)
    ├── cssjs/
    │   ├── default.css
    │   ├── default.js
    │   ├── light.css
    │   ├── light.js
    │   ├── dark.css
    │   └── dark.js
    ├── icons/
    │   ├── user.svg
    │   ├── phone.svg
    │   └── pet.png
    ├── images/
    │   ├── logo.png
    │   ├── favicon.png
    │   ├── stephen.png
    │   ├── joy.png
    │   ├── tate.png
    │   ├── quinn.png
    │   ├── luna.png
    │   ├── sunny.png
    │   └── zelda.png
    └── templates/
        ├── navs/
        │   ├── top.jinja
        │   ├── left.jinja
        │   ├── right.jinja
        │   └── footer.jinja
        └── sections/
            ├── divider.jinja
            ├── gallery.jinja
            ├── hero.jinja
            ├── markdown.jinja
            ├── pagelist.cards.jinja
            ├── pagelist.table.jinja
            ├── pagelist.tiles.jinja
            └── map.jinja
```



# Generation Request
Attached will be a zip file with a sample set of config files.  Please understand the requirements layed out here, then generate content for:

- all .jinja files found in /src/templates/navs/* and /src/templates/sections/*
    - follow the instructions found in the file comments 
    - leave the file comments unchanged

- all .css and .js files found in /src/cssjs/* to style the website.
    - the style should be simple and modern
    - use javascript to make the pages feel interactive and responsive
    - remember, this must be a static website, so no server calls allowed

- fully generate the python engine, found in /src/sitegen.py
    - if you want / need to break into more than one .py file, create a subfolder: /src/sitegen/ and store new files there
    - make sure the sitegen.py always operates on a relative path, starting from it's own /src/ directory. I.e., set a rootpath Path() object = the sitegen.py __file__ location.
    - save all sitegen.py output to a timestamped log file, in a /src/sitegen/logs/ logfile.


# Post-AI Fixes:

- the blogs.html is built correctly, except all the blog content needs to be nexted under the /blogs/* subdirectory. Today the blogs are all returning 404 errors when clicked.

- the blog "yaml front matter" definition includes: `navs: ["top"]` however the blog page is devoid of any nav sections, neither top nor footer nor left nor right.

- several pages specify a left or right nav bar, which should slide out from the left or right when clicking on a visible handle. However I don't see any left or right nav sections, at all.



- please have the sitegen.py always replace .html files without prompting.  We will use github for version control.