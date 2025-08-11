import re, hashlib
from urllib.parse import urlparse

def is_external_url(url: str) -> bool:
    return bool(url) and urlparse(url).scheme in ("http", "https")

def minify_html(html: str) -> str:
    # Preserve pre/code/script/style blocks
    blocks = []
    def store(m):
        blocks.append(m.group(0))
        return f"§§B{len(blocks)-1}§§"

    h = re.sub(r'(<(pre|code|script|style)[\s\S]*?</\2>)', store, html, flags=re.I)
    h = re.sub(r"<!--(?!\[if).*?-->", "", h, flags=re.S)   # strip normal comments
    h = re.sub(r">\s+<", "><", h)                          # collapse gaps between tags
    h = re.sub(r"\s{2,}", " ", h)                          # collapse long runs of ws

    def restore(m): return blocks[int(m.group(1))]
    h = re.sub(r"§§B(\d+)§§", restore, h)
    return h

def replace_image_tokens(html: str, base_url: str = "/content/_images/") -> str:
    # {{filename.ext}} -> /content/_images/filename.ext
    return re.sub(r"\{\{\s*([^\}\s]+)\s*\}\}", lambda m: f"{base_url}{m.group(1)}", html)

def content_hash(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()[:10]
