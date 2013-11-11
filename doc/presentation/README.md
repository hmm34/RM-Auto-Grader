### Automatic Grader Presentation

This is for our second project presentation. It's written in markdown
and rendered using [Reveal.js](https://github.com/hakimel/reveal.js).

#### Editing

Basically, two lines separate slides. Hashtags make the text bold and
increase the font size. Asteriks are used for unordered lists, numbers
for ordered lists. There is more in-depth documentation 
[here](http://daringfireball.net/projects/markdown/).

Changing the theme can be acommplished in the presentation.html file.
Any edit to the slides will be done in the presentation.md file.

#### Viewing

The easiest way to view the presentation is to use pythons built in HTTP
server.

````sh
$ cd presentations
$ python -m SimpleHTTPServer
Serving HTTP 0.0.0.0 port 8000 ...
```

Then in a web browser load <http://localhost:8000/presentation.html>.

Another option is to view it through github, but it's not as flashy.
