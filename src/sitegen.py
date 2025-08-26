#!/usr/bin/env python3

import os
import sys
import yaml
import re
from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import logging

try:
    import markdown
except ImportError:
    print("Installing required packages...")
    os.system("pip install markdown jinja2 pyyaml")
    import markdown

class SiteGenerator:
    def __init__(self):
        self.root_path = Path(__file__).parent.parent
        self.src_path = Path(__file__).parent
        self.templates_path = self.src_path / "templates"
        self.logs_path = self.src_path / "sitegen" / "logs"
        
        # Create logs directory if it doesn't exist
        self.logs_path.mkdir(parents=True, exist_ok=True)
        
        # Setup logging
        log_file = self.logs_path / f"sitegen_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Setup Jinja2 environment
        self.jinja_env = Environment(loader=FileSystemLoader(self.templates_path))
        
        # Load site config
        self.site_config = self.load_site_config()
        
    def load_site_config(self):
        """Load site-wide configuration from index.yaml"""
        index_file = self.root_path / "index.yaml"
        if index_file.exists():
            with open(index_file, 'r') as f:
                config = yaml.safe_load(f)
                return config.get('site', {})
        return {}
    
    def parse_markdown_frontmatter(self, content):
        """Parse YAML frontmatter from markdown content"""
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    # Handle the list format in frontmatter
                    frontmatter_text = parts[1].strip()
                    if frontmatter_text.startswith('-'):
                        # Convert list format to dict format
                        lines = frontmatter_text.split('\n')
                        yaml_dict = {}
                        for line in lines:
                            line = line.strip()
                            if line.startswith('- ') and ':' in line:
                                # Remove comments
                                if '#' in line:
                                    line = line.split('#')[0].strip()
                                key_value = line[2:].split(':', 1)
                                if len(key_value) == 2:
                                    key = key_value[0].strip()
                                    value = key_value[1].strip().strip('"').strip("'")
                                    
                                    # Handle array values like ["top", "footer"]
                                    if value.startswith('[') and value.endswith(']'):
                                        # Parse as array
                                        array_content = value[1:-1].strip()
                                        if array_content:
                                            items = [item.strip().strip('"').strip("'") for item in array_content.split(',')]
                                            yaml_dict[key] = items
                                        else:
                                            yaml_dict[key] = []
                                    # Handle date parsing
                                    elif key == 'date' and value.isdigit() == False:
                                        try:
                                            # Try to parse as date
                                            from datetime import datetime
                                            if '-' in value:
                                                yaml_dict[key] = value.split()[0]  # Take just the date part
                                            else:
                                                yaml_dict[key] = value
                                        except:
                                            yaml_dict[key] = value
                                    else:
                                        yaml_dict[key] = value
                        frontmatter = yaml_dict
                    else:
                        frontmatter = yaml.safe_load(frontmatter_text)
                    
                    markdown_content = parts[2].strip()
                    return frontmatter, markdown_content
                except yaml.YAMLError as e:
                    self.logger.error(f"Error parsing frontmatter: {e}")
                    return {}, content
        return {}, content
    
    def get_page_files(self, subfolder=None):
        """Get all markdown files in a subfolder with their metadata"""
        if subfolder:
            folder_path = self.root_path / subfolder
        else:
            folder_path = self.root_path
            
        if not folder_path.exists():
            return []
            
        pages = []
        for md_file in folder_path.glob("*.md"):
            with open(md_file, 'r') as f:
                content = f.read()
                frontmatter, markdown_content = self.parse_markdown_frontmatter(content)
                
                # Extract date from filename if not in frontmatter
                date_match = re.match(r'(\d{4}-\d{2}-\d{2})', md_file.name)
                if date_match and 'date' not in frontmatter:
                    frontmatter['date'] = date_match.group(1)
                
                pages.append({
                    'file_path': md_file,
                    'frontmatter': frontmatter,
                    'content': markdown_content,
                    'html_path': md_file.with_suffix('.html')
                })
        
        return pages
    
    def sort_pages(self, pages, sort_key="date_desc"):
        """Sort pages based on the sort key"""
        if not sort_key:
            return pages
            
        parts = sort_key.split('_')
        field = parts[0] if parts else 'date'
        direction = parts[1] if len(parts) > 1 else 'desc'
        
        def get_sort_value(page):
            value = page['frontmatter'].get(field, '')
            if field == 'date' and isinstance(value, str):
                try:
                    return datetime.strptime(value, '%Y-%m-%d')
                except:
                    return datetime.min
            return value or ''
        
        reverse = direction == 'desc'
        return sorted(pages, key=get_sort_value, reverse=reverse)
    
    def render_template(self, template_name, context):
        """Render a Jinja2 template with context"""
        try:
            template = self.jinja_env.get_template(template_name)
            return template.render(**context)
        except Exception as e:
            self.logger.error(f"Error rendering template {template_name}: {e}")
            return f"<!-- Error rendering template {template_name}: {e} -->"
    
    def process_sections(self, sections, page_context):
        """Process all sections for a page"""
        rendered_sections = []
        
        for section in sections:
            section_type = section.get('type')
            if not section_type:
                continue
                
            template_file = f"sections/{section_type}.jinja"
            
            # Prepare section context
            section_context = {**page_context, **section}
            
            # Special handling for pagelist sections
            if section_type.startswith('pagelist.'):
                subfolder = section.get('subfolder')
                if subfolder:
                    pages = self.get_page_files(subfolder)
                    sort_key = section.get('sort', 'date_desc')
                    pages = self.sort_pages(pages, sort_key)
                    
                    limit = section.get('limit')
                    if limit:
                        pages = pages[:limit]
                    
                    section_context['pages'] = pages
            
            # Render markdown content if present
            if 'content' in section:
                md = markdown.Markdown(extensions=['extra'])
                section_context['content_html'] = md.convert(section['content'])
            
            rendered_html = self.render_template(template_file, section_context)
            rendered_sections.append(rendered_html)
        
        return '\n'.join(rendered_sections)
    
    def generate_html_page(self, page_config, sections, output_path):
        """Generate a complete HTML page"""
        # Prepare page context
        context = {
            'site': self.site_config,
            'page': page_config,
            'current_date': datetime.now().strftime('%Y-%m-%d')
        }
        
        # Process navigation templates
        navs = page_config.get('navs', [])
        nav_html = {}
        
        # Add navigation context to template context first
        context['nav_html'] = nav_html
        context['has_left_nav'] = 'left' in navs
        context['has_right_nav'] = 'right' in navs
        
        if navs and isinstance(navs, list):
            for nav in navs:
                if isinstance(nav, str):  # Ensure nav is a string
                    nav_template = f"navs/{nav}.jinja"
                    nav_html[nav] = self.render_template(nav_template, context)
        
        # Update navigation context
        context['nav_html'] = nav_html
        
        # Process sections
        sections_html = self.process_sections(sections, context)
        
        # Left nav hamburger is now part of the slide-out itself
        left_nav_button = ''
        
        # Create basic HTML structure
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_config.get('title', self.site_config.get('title', 'Site'))}</title>
    <meta name="description" content="{page_config.get('description', '')}">
    <meta name="keywords" content="{page_config.get('keywords', '')}">
    <meta name="author" content="{page_config.get('author', '')}">
    <link rel="icon" type="image/png" href="/src/images/favicon.png">
    <link rel="stylesheet" href="/src/cssjs/{self.site_config.get('themes', {}).get('default', {}).get('css', 'default.css')}">
</head>
<body>
    {left_nav_button}
    {nav_html.get('top', '')}
    {nav_html.get('left', '')}
    {nav_html.get('right', '')}
    
    <main>
        {sections_html}
    </main>
    
    
    {nav_html.get('footer', '')}
    
    <script src="/src/cssjs/{self.site_config.get('themes', {}).get('default', {}).get('js', 'default.js')}"></script>
</body>
</html>"""
        
        # Write HTML file
        with open(output_path, 'w') as f:
            f.write(html_content)
        
        self.logger.info(f"Generated: {output_path}")
    
    def process_yaml_file(self, yaml_file):
        """Process a YAML configuration file"""
        with open(yaml_file, 'r') as f:
            config = yaml.safe_load(f)
        
        page_config = config.get('page', {})
        sections = config.get('sections', [])
        
        # Generate HTML file
        html_file = yaml_file.with_suffix('.html')
        self.generate_html_page(page_config, sections, html_file)
    
    def process_markdown_file(self, md_file):
        """Process a Markdown file"""
        with open(md_file, 'r') as f:
            content = f.read()
        
        frontmatter, markdown_content = self.parse_markdown_frontmatter(content)
        
        # Convert markdown to HTML
        md = markdown.Markdown(extensions=['extra'])
        content_html = md.convert(markdown_content)
        
        # Create a markdown section with title, description, and content
        sections = [{
            'type': 'markdown',
            'title': frontmatter.get('title'),
            'description': frontmatter.get('description'),
            'content_html': content_html
        }]
        
        # Generate HTML file
        html_file = md_file.with_suffix('.html')
        self.generate_html_page(frontmatter, sections, html_file)
    
    def generate_site(self):
        """Generate the entire site"""
        self.logger.info("Starting site generation...")
        
        # Process YAML files in root directory
        for yaml_file in self.root_path.glob("*.yaml"):
            self.process_yaml_file(yaml_file)
        
        # Process Markdown files in root and subdirectories
        for md_file in self.root_path.rglob("*.md"):
            # Skip README.md
            if md_file.name == "README.md":
                continue
            
            # Skip files in /src/ folder
            if "src" in md_file.parts:
                continue
            
            # Skip if there's a corresponding YAML file
            yaml_file = md_file.with_suffix('.yaml')
            if not yaml_file.exists():
                self.process_markdown_file(md_file)
        
        self.logger.info("Site generation completed!")
    
    def start_test_server(self, port=8000):
        """Start a local test server"""
        import http.server
        import socketserver
        import webbrowser
        
        root_path = self.root_path
        
        class Handler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=root_path, **kwargs)
        
        with socketserver.TCPServer(("", port), Handler) as httpd:
            url = f"http://localhost:{port}"
            print(f"Server running at: {url}")
            webbrowser.open(url)
            httpd.serve_forever()

def main(start_test_server:bool = False):
    generator = SiteGenerator()
    generator.generate_site()
    if start_test_server: generator.start_test_server()

if __name__ == "__main__":
    main()
    
