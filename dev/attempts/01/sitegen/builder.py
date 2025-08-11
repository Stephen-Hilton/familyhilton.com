import os, re, shutil, datetime
from pathlib import Path
from typing import Dict
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
try:
    import markdown
    _HAS_MD = True
except Exception:
    _HAS_MD = False

from .utils import minify_html, replace_image_tokens

LAYOUT_TEMPLATES = {
    "home": "home.html",
    "standard": "standard.html",
    "blog_index": "blog_index.html",
    "blog_post": "blog_post.html",
    "people_index": "people_index.html",
    "profile_page": "profile_page.html",
    "sitemap": "sitemap.html",
}

class SiteBuilder:
    def __init__(self, root: Path):
        self.root = Path(root)
        self.content_dir = self.root / "content"
        self.pages_dir = self.root / "pages"
        self.global_dir = self.content_dir / "_global"
        self.images_dir = self.content_dir / "_images"
        self.templates_dir = (self.root / "sitegen" / "templates"
                              if (self.root / "sitegen" / "templates").exists()
                              else Path(__file__).with_suffix("").parent / "templates")

        self.env = Environment(
            loader=FileSystemLoader(str(self.templates_dir)),
            autoescape=select_autoescape(["html", "xml"]),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.env.globals.update({
            "now": datetime.datetime.utcnow().isoformat(),
            "asset_stamp": datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S"),
        })

    # ---------- Commands ----------
    def init_site(self):
        (self.global_dir).mkdir(parents=True, exist_ok=True)
        (self.images_dir).mkdir(parents=True, exist_ok=True)

        # Minimal starter content (only if missing)
        (self.content_dir / "index.yaml").write_text(
            "meta:\n"
            "  title: 'Hilton Family'\n"
            "  description: 'Updates, projects, and adventures.'\n"
            "  date: '2025-08-11'\n"
            "layout: 'home'\n"
            "hero:\n"
            "  headline: 'Welcome to our site'\n"
            "  subheadline: 'Simple, fast, and friendly.'\n"
            "  background_image: '{{banner.svg}}'\n"
            "sections:\n"
            "  - type: 'markdown'\n"
            "    heading: 'Hello'\n"
            "    body_md: 'This is a starter site. Edit content in /content.'\n",
            encoding="utf-8"
        )
        (self.content_dir / "blogs.yaml").write_text(
            "meta: { title: 'Blog', description: 'Notes', date: '2025-08-11' }\n"
            "layout: 'blog_index'\n", encoding="utf-8"
        )
        (self.content_dir / "people.yaml").write_text(
            "meta: { title: 'People', description: 'Meet us', date: '2025-08-11' }\n"
            "layout: 'people_index'\n", encoding="utf-8"
        )
        (self.content_dir / "blogs" / "2025" / "08").mkdir(parents=True, exist_ok=True)
        (self.content_dir / "blogs" / "2025" / "08" / "Author-Name--Hello-World.md").write_text(
            "# Hello World\n\nSample post.", encoding="utf-8"
        )
        (self.content_dir / "people").mkdir(parents=True, exist_ok=True)
        (self.content_dir / "people" / "Quinn.md").write_text("# Quinn\n\nBio.", encoding="utf-8")

        (self.global_dir / "global.yaml").write_text(
            "site:\n"
            "  name: 'Hilton Family'\n"
            "  base_url: ''\n"
            "assets:\n"
            "  css: ['/content/_global/css/main.css']\n"
            "  js:  ['/content/_global/javascript/main.js']\n"
            "seo:\n"
            "  default_title_suffix: ' — Hilton Family'\n",
            encoding="utf-8"
        )
        (self.global_dir / "top_nav.yaml").write_text(
            "version: 1\n"
            "brand: { site_name: 'Hilton Family', href: '/index.html' }\n"
            "menus:\n"
            "  left:\n"
            "    - { type: link, label: Home,   href: /index.html }\n"
            "    - { type: link, label: Blog,   href: /pages/blogs.html }\n"
            "    - { type: link, label: People, href: /pages/people.html }\n"
            "  right: []\n", encoding="utf-8"
        )
        (self.global_dir / "css").mkdir(parents=True, exist_ok=True)
        (self.global_dir / "css" / "main.css").write_text(
            "body{font-family:system-ui;background:#0b1020;color:#e9ecf1;margin:0}"
            ".container{max-width:1100px;margin:0 auto;padding:24px}"
            ".topbar{position:sticky;top:0;padding:12px 24px;background:#1114;backdrop-filter:blur(6px);display:flex;justify-content:space-between}"
            ".grid{display:grid;gap:16px}.grid.cards{grid-template-columns:repeat(auto-fill,minmax(260px,1fr))}"
            ".card{background:#121933;padding:20px;border-radius:16px}", encoding="utf-8"
        )
        (self.global_dir / "javascript").mkdir(parents=True, exist_ok=True)
        (self.global_dir / "javascript" / "main.js").write_text("// placeholder\n", encoding="utf-8")
        (self.images_dir / "banner.svg").write_text(
            "<svg xmlns='http://www.w3.org/2000/svg' width='1600' height='400'>"
            "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
            "<stop offset='0' stop-color='#0ea5e9'/>"
            "<stop offset='1' stop-color='#1e3a8a'/>"
            "</linearGradient></defs><rect width='100%' height='100%' fill='url(#g)'/></svg>",
            encoding="utf-8"
        )

    def clean(self):
        # Remove output pages and index.html (idempotent build)
        if self.pages_dir.exists():
            shutil.rmtree(self.pages_dir)
        idx = self.root / "index.html"
        if idx.exists():
            idx.unlink()

    def build(self):
        self._require(self.content_dir.exists(), f"Missing content directory: {self.content_dir}")
        self._require(self.templates_dir.exists(), f"Missing templates directory: {self.templates_dir}")

        self.clean()

        globals_cfg = self._yaml(self.global_dir / "global.yaml") or {}
        top_nav = self._yaml(self.global_dir / "top_nav.yaml") or None

        # index
        index_yaml = self.content_dir / "index.yaml"
        if index_yaml.exists() and not self._is_draft(index_yaml):
            ctx = self._page_ctx(index_yaml, globals_cfg, top_nav)
            html_out = self._render(ctx)
            (self.root / "index.html").write_text(html_out, encoding="utf-8")

        # other yaml pages
        for yml in sorted(self.content_dir.glob("*.yaml")):
            if yml.name == "index.yaml" or self._is_draft(yml):
                continue
            ctx = self._page_ctx(yml, globals_cfg, top_nav)
            out_path = self.pages_dir / (yml.stem + ".html")
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(self._render(ctx), encoding="utf-8")

            # render subpages if content/<stem> folder exists (blogs, people, etc.)
            subdir = self.content_dir / yml.stem
            if subdir.exists() and subdir.is_dir():
                self._render_subpages(yml.stem, subdir, globals_cfg, top_nav)

        # extras
        (self.root / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: /sitemap.xml\n", encoding="utf-8")
        self._sitemap(globals_cfg)

    # ---------- helpers ----------
    def _yaml(self, p: Path) -> Dict:
        if not p.exists():
            return {}
        try:
            return yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        except Exception as e:
            raise SystemExit(f"YAML error in {p}: {e}")

    def _is_draft(self, yml: Path) -> bool:
        return bool((self._yaml(yml) or {}).get("draft", False))

    def _page_ctx(self, yml: Path, globals_cfg: Dict, top_nav: Dict) -> Dict:
        data = self._yaml(yml)
        ctx = {
            "meta": data.get("meta", {}),
            "layout": data.get("layout", "standard"),
            "sections": data.get("sections", []),
            "hero": data.get("hero"),
            "globals": globals_cfg,
            "top_nav": top_nav,
            "page_name": yml.stem,
        }
        if yml.stem == "blogs":
            ctx.update(self._blogs_index_ctx())
        if yml.stem == "people":
            ctx.update(self._people_index_ctx())
        return ctx

    def _render(self, ctx: Dict) -> str:
        tpl_name = LAYOUT_TEMPLATES.get(ctx.get("layout", "standard"), "standard.html")
        tpl = self.env.get_template(tpl_name)
        html = tpl.render(**ctx)
        html = replace_image_tokens(html, base_url="/content/_images/")
        return minify_html(html)

    def _render_subpages(self, stem: str, subdir: Path, globals_cfg: Dict, top_nav: Dict):
        for md in sorted(subdir.rglob("*.md")):
            rel = md.relative_to(subdir)
            out_dir = self.pages_dir / stem / rel.parent
            out_dir.mkdir(parents=True, exist_ok=True)

            if stem == "blogs":
                title, author, date = self._parse_blog_filename(md)
                layout = "blog_post"
            elif stem == "people":
                title = md.stem.replace("-", " ").title()
                author = None; date = None
                layout = "profile_page"
            else:
                title = md.stem.replace("-", " ").title()
                author = None; date = None
                layout = "standard"

            body_html = self._md(md.read_text(encoding="utf-8"))

            ctx = {
                "meta": {"title": title, "author": author, "date": date},
                "layout": layout,
                "sections": [{"type": "html", "html": body_html}],
                "hero": None,
                "globals": globals_cfg,
                "top_nav": top_nav,
                "page_name": md.stem,
            }
            tpl = self.env.get_template(LAYOUT_TEMPLATES.get(layout, "standard.html"))
            raw = tpl.render(**ctx)
            (out_dir / md.with_suffix(".html").name).write_text(
                minify_html(replace_image_tokens(raw, base_url="/content/_images/")),
                encoding="utf-8"
            )

    def _md(self, text: str) -> str:
        if _HAS_MD:
            return markdown.markdown(text, extensions=["extra", "sane_lists", "toc", "codehilite"])
        return "<p>" + text.replace("\n\n", "</p><p>") + "</p>"

    def _parse_blog_filename(self, md: Path):
        # Expect /blogs/YYYY/MM/Author-Name--Title-HTML-Friendly.md
        try:
            year = md.parent.parent.name
            month = md.parent.name
        except Exception:
            year = month = ""
        stem = md.stem
        if "--" in stem:
            author_part, title_part = stem.split("--", 1)
        else:
            parts = re.split(r"\s{2,}", stem)
            author_part, title_part = (parts[0], " ".join(parts[1:]) if len(parts) > 1 else stem)
        author = author_part.replace("-", " ").strip().title()
        title = title_part.replace("-", " ").strip().title()
        date = f"{year}-{month}-01" if year and month else None
        return title, author, date

    def _blogs_index_ctx(self) -> Dict:
        posts = []
        base = self.content_dir / "blogs"
        if base.exists():
            for md in sorted(base.rglob("*.md")):
                title, author, date = self._parse_blog_filename(md)
                rel = md.relative_to(base).with_suffix(".html")
                href = f"/pages/blogs/{rel.as_posix()}"
                posts.append({"title": title, "author": author, "date": date, "href": href})
            posts.sort(key=lambda x: (x.get("date") or "", x["title"]), reverse=True)
        return {"posts": posts}

    def _people_index_ctx(self) -> Dict:
        people = []
        base = self.content_dir / "people"
        if base.exists():
            for md in sorted(base.glob("*.md")):
                name = md.stem.replace("-", " ").title()
                href = f"/pages/people/{md.with_suffix('.html').name}"
                avatar = None
                for ext in ("png", "jpg", "jpeg", "svg"):
                    cand = self.images_dir / f"{md.stem.lower()}_avatar.{ext}"
                    if cand.exists():
                        avatar = f"/content/_images/{cand.name}"
                        break
                people.append({"name": name, "href": href, "avatar": avatar})
        return {"people": people}

    def _sitemap(self, globals_cfg: Dict):
        base_url = (globals_cfg.get("site", {}) or {}).get("base_url", "").rstrip("/")
        urls = []
        if (self.root / "index.html").exists():
            urls.append(f"{base_url}/index.html".replace("//", "/"))
        if self.pages_dir.exists():
            for p in self.pages_dir.rglob("*.html"):
                urls.append(f"{base_url}/{p.relative_to(self.root).as_posix()}".replace("//", "/"))

        lines = ["<?xml version='1.0' encoding='UTF-8'?>",
                 "<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>"]
        for u in urls:
            lines.append(f"  <url><loc>{u}</loc></url>")
        lines.append("</urlset>")
        (self.root / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")

    @staticmethod
    def _require(cond: bool, msg: str):
        if not cond:
            raise SystemExit(msg)
