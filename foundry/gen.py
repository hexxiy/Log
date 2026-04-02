import os
import re

def markdown_to_html(text):
    # Very basic parser for # headers and double newlines for paragraphs
    # No external library needed. Sovereign.
    html = []
    blocks = re.split(r'\n\n+', text)
    for block in blocks:
        if block.startswith('# '):
            html.append(f"<h1>{block[2:]}</h1>")
        else:
            html.append(f"<p>{block}</p>")
    return "\n".join(html)

def build():
    # Ensure directories exist
    os.makedirs('foundry/content', exist_ok=True)
    
    posts_md = [f for f in os.listdir('foundry/content') if f.endswith('.md')]
    for post in posts_md:
        with open(f'foundry/content/{post}', 'r') as f:
            content = markdown_to_html(f.read())
        
        # Build the HTML document
        html = f"""<!doctype html>
<html>
<head><link rel="stylesheet" href="foundry/static/style.css"></head>
<body><main>
<nav><a href="index.html">← Back to Index</a></nav>
{content}</main></body>
</html>"""
        
        # Write to the root of the repo (where GitHub Pages picks it up)
        with open(f'{post.replace(".md", ".html")}', 'w') as f:
            f.write(html)
        print(f"Built {post} -> {post.replace('.md', '.html')}")

if __name__ == "__main__":
    build()
