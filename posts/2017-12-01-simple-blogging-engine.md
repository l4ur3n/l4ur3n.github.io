# Simple Static Blogging Engine in Python

A [static site generator](https://www.staticgen.com/) is usually a program for taking some kind of text input, 
and converting it into HTML files which can be used to make a website. I decided I wanted to use one to create 
my blog.
It seems like there are thousands of them available, and I'm bad at making decisions.
So obviously, I just went ahead and made my own! My requirements are simple - I just want to be able
to write posts in [Markdown](https://daringfireball.net/projects/markdown/syntax), and have them rendered
to static HTML files suitable for hosting on Github Pages, or anywhere else I might want to put them.
The other reason I made my own is that I hate reading documentation 😂.

I chose to write this project in Python, since that's what I'm most comfortable with (I'll leave the x86
assembly rewrite for another project...). This certainly isn't the best code I've ever written, but I'm 
mainly just publising it to show how easy it can be to get a simple project up-and-running with Python.
The main structure of the project looks like this:

```
l4ur3n.github.io/
	posts/
		2017-11-30-hello-world.md
		2017-12-01-simple-blogging-engine.md
	blog/
		hello-world.html               # generated
		simple-blogging-engine.html    # generated
	static/
		main.css
	template.html
	index.html       # generated
	render.py
```

`posts/` is where I can write posts in Markdown. Note that the date is embedded into the filename, along with
the ["slug"](https://en.wikipedia.org/wiki/Slug_%28publishing%29). `template.html` contains the main web
design for the site, which I also made from scratch.

Here's the main code (I put it in a gist in case I update the code in the repo later):

<script src="https://gist.github.com/l4ur3n/3f8fe390a7dcefc553a0e8f1f644c355.js"></script>

When I run `./render.py`, the first thing it does is iterate through all the Markdown files in the `posts/` 
directory using the [glob](https://docs.python.org/3/library/glob.html) module. As the documentation says, this 
module is for "Unix style pathname pattern expansion". That might sound complicated, but it's really quite 
simple once you get used to it. In my code, I use `glob("posts/*.md")`. This means "Find all files in the 
`posts/` directory which end in `.md`" - the star character effectively means "any letters can go here".

Then, for each file, it parses the file name using some really horrible code in order to extract the date and 
slug information from it. Then it reads the file, extracts the title, and then runs it through the
[mistune](http://mistune.readthedocs.io/en/latest/) Python module. This renders the markdown markup to an HTML 
file (using the template I made) and puts it in the `blog/` directory.

Finally, the `index.html` page is generated, which will contain links to each individual blog post. This is the 
page that visitors should see when they first visit the blog.

As you might have noticed by now, you are currently reading a blog post which was created with the code above!
You can see the current status of the code here: https://github.com/l4ur3n/l4ur3n.github.io

Thanks for reading my first blog post! If you have any feedback, you can open a github issue or contact me on 
[twitter](https://twitter.com/l4ur3n_h).
