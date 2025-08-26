# AI Context Summary - Static Site Generator Project

## Project Overview
Python-based static site generator (`sitegen.py`) that converts YAML configuration files and Markdown content into static HTML websites. Built for simplicity and non-technical user operation.

## Current Status
- **Working sitegen.py engine** - Fully functional with logging, Jinja2 templating, and multi-format processing
- **Modified to skip README.md and /src/ folder** during processing to prevent unwanted HTML generation
- **Location**: `/Users/stephen.hilton/Dev/familyhilton.com/`

## Architecture

### File Processing Logic
1. **YAML files** (*.yaml) → HTML pages with structured sections
2. **Markdown files** (*.md) → HTML pages via markdown.jinja template
3. **Priority**: YAML takes precedence over MD if both exist with same name
4. **Exclusions**: README.md and entire /src/ folder are skipped

### Directory Structure
```
root/
├── *.yaml              # Page configurations
├── *.md                # Markdown content (if no corresponding .yaml)
├── [folders]/          # Subfolders with *.md files (blogs/, people/, pets/)
└── src/                # Source files (never modified)
    ├── sitegen.py      # Main engine
    ├── cssjs/          # Themes (default.css/js, light, dark)
    ├── images/         # All images referenced as /src/images/
    ├── icons/          # UI icons
    └── templates/      # Jinja2 templates
        ├── navs/       # Navigation components
        └── sections/   # Content section types
```

### Configuration Format

#### YAML Pages
```yaml
page:
  title: "Page Title"
  description: "Description"
  author: "Author"
  navs: ["top", "footer", "left"]
  
sections:
  - type: "hero"
    title: "Welcome"
  - type: "markdown" 
    content: "**Markdown content**"
```

#### Markdown Pages
```markdown
---
- title: "Page Title"
- description: "Description"
- author: "Author"
---

Markdown content here
```

### Section Types Available
- `hero` - Hero banners with background images
- `markdown` - Rendered markdown content
- `features` - Feature grids with icons
- `pagelist.cards` - Card-based page listings from subfolders
- `pagelist.tiles` - Tile-based page listings
- `divider` - Horizontal separators

### Key Features
- **Jinja2 templating** with section-based architecture
- **Multiple themes** (default, light, dark) via CSS/JS files
- **YAML frontmatter parsing** with list format support
- **Automatic page listing** from subfolders (blogs/, people/, etc.)
- **Responsive design** with navigation components
- **Timestamped logging** in src/sitegen/logs/
- **Auto-dependency installation** (PyYAML, Jinja2, Markdown)

### Site Configuration
Located in `index.yaml` under `site:` section:
- Site title, description, favicon
- Theme definitions (CSS/JS mappings)
- Navigation page order
- Global keywords for SEO

### Usage
```bash
python3 src/sitegen.py
```
Processes all .yaml and .md files, generates corresponding .html files in same locations.

### Recent Modifications
- Added exclusion logic for README.md files
- Added exclusion logic for entire /src/ folder
- Prevents documentation and source files from being processed into HTML

### Dependencies
- Python 3.6+
- PyYAML (auto-installed)
- Jinja2 (auto-installed) 
- Markdown (auto-installed)

### Development Context
- Built using AWS Q with Claude 4.0 LLM assistance
- Designed for family website use case
- Optimized for non-technical users
- Generates static files suitable for GitHub Pages, S3, Netlify, etc.