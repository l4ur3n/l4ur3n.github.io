#!/usr/bin/python3

from glob import glob
from datetime import datetime
import mistune

template = open("template.html", "r").read()

posts = []

markdown = mistune.Markdown(escape=True)

for post_file in glob("posts/*.md"):
	post = {}
	
	# horribly hacky parsing...
	name_parts = post_file.split("/")[-1].split(".")[0].split("-")
	year, month, day = [int(n) for n in name_parts[:3]]
	post["date"] = datetime(year, month, day)
	post["slug"] = "-".join(name_parts[3:])
	
	raw_content = open(post_file, "r").read()
	post["title"] = raw_content.split("\n")[0].lstrip("# ")
	
	with open("blog/{}.html".format(post["slug"]), "w") as html:
		html.write(template.format(post["title"], markdown(raw_content)))
	
	posts.append(post)

posts.sort(key=lambda p: p["date"], reverse=True) # chronological sort

with open("index.html", "w") as index:
	content = ["<h1>Blog Posts</h1>"]
	entry = """<p style="margin: 0;"><a href="blog/{}.html">{}</a><em> - {}</em></p>"""
	for post in posts:
		date =  post["date"].strftime("%b %d %Y")
		content.append(entry.format(post["slug"], post["title"], date))
	index.write(template.format("Blog", "\n\t\t\t".join(content)))
