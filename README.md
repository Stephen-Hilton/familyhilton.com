# Static Site Generator

A Python-based static site generator that converts YAML configuration files and Markdown content into a complete static website.

To use: 
1. Modify the .yaml config files in the project root, one yaml per webpage.
2. Execute the `/src/sitegen.py` script to transform config files in html webpages.
3. Optionally, execute `/src/webserver_start.py` to launch a local webserver and test your page.

Done!

# Does the world need another static-webpage builder?  

Maybe not, but those that I found existing were overly complicated for my use-case.  I wanted something static, free, and dead-simple, making it easy for non-technical folks to operate - something that could be operated by most members of a family. 

It was also a chance to use AWS-Q with Claude 4.0 LLM - color me impressed.  It took me several hours to build out my desired structures for yaml and markdown, and about 10 minutes for Q to create the entire working application, with about 80% accuracy, and maybe another few hours of prompting for various fixes and updates to arrive at what you see here. 

## Features

- **YAML Configuration**: Define page structure and content using YAML files
- **Markdown Support**: Write content in Markdown with YAML frontmatter
- **Jinja2 Templates**: Flexible templating system for layouts and components
- **Multiple Themes**: Built-in support for default, light, and dark themes
- **Responsive Design**: Modern, mobile-friendly CSS and JavaScript
- **Interactive Elements**: Smooth animations, navigation, and user interactions
- **Blog Support**: Automatic blog post listing and sorting
- **Static Output**: Generates pure HTML/CSS/JS for hosting anywhere

## Usage

### Generate the Site

```bash
python3 src/sitegen.py
```

This will:
1. Process all `.yaml` files in the root directory
2. Convert `.md` files to HTML (if no corresponding `.yaml` exists)
3. Create a timestamped log file in `src/sitegen/logs/`

### Sample File Structure

```
root/
├── index.yaml              # Homepage configuration
├── about.yaml              # About page configuration
├── blogs.yaml              # Blog listing page
├── blogs/                  # Individual blog posts
│   └── *.md                # Markdown blog posts
├── people/                 # People profiles
│   └── *.md                # Markdown profiles
└── src/                    # Source files (don't modify)
    ├── sitegen.py          # Main generator script
    ├── webserver_start.py  # local webserver for testing
    ├── cssjs/              # CSS and JavaScript themes
    ├── images/             # Site images
    ├── icons/              # UI icons
    └── templates/          # Jinja2 templates
        ├── navs/           # Navigation templates
        └── sections/       # Content section templates
```

### Configuration Files

#### YAML Pages (`*.yaml`)

YAML pages will always have 2 sections: 

- **page**: configuration details about the page. These sections should be consistent from page to page (including in front matter of markdown files).
- **sections**: section type and config details about that section.  Each section may have a different set of components, with different config options. 

For example:

```yaml
page:
  title: "My Page"  
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

Note that the `index.yaml` config file has one additional section: 

```yaml
site:  
  title: "Your website name"
  description: "Short description of your website" 
  favicon: /image/favicon.png  # browser tab icon
  keywords: "family, blog, updates, projects, adventures" # for SEO
  nav_pages: ['about','people','pets','blogs'] # order / list of pages for navs. 
```

#### Markdown Pages (`*.md`)

Markdown will have a embedded yaml document (called "front matter") at the beginning, followed by  arbitrary markdown content.  Note, that the title and description will be added to the top of the output html, so you don't need to add that twice. 

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

Markdown pages are basically the same as yaml pages with one section type, set to "markdown".


### Available Section Types

- `hero`: Hero banner with background image and call-to-action buttons
- `markdown`: Rendered markdown content
- `features`: Feature grid with icons and descriptions
- `pagelist.cards`: Card-based listing of pages from a subfolder
- `pagelist.tiles`: Tile-based listing of pages from a subfolder
- `divider`: Simple horizontal rule separator

### Themes

Three built-in themes available:
- **Default**: Balanced colors and modern design
- **Light**: Bright, clean appearance
- **Dark**: Dark mode with subtle glow effects

Configure in `index.yaml`:

```yaml
site:
  themes:
    default:
      css: default.css
      js: default.js
```

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

All generation activity is logged to timestamped files in `src/sitegen/logs/` for debugging and monitoring.