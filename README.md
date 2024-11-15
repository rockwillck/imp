# Imp
Highly opinionated blogging

## What is Imp?
Imp is a tool for generating beautiful blogs.  

Because Imp was built for [Pine](https://pine.hwalgi.org), it's incredibly opinionated.  

That's not to say you can't customize Imp sites: the entirety of the sites styling is summarized in `style.css` and `article.css`.

## .imp
The core file of an Imp site is `.imp`. It's a very simple format:
```imp
First line = title
Second line = subtitle
Third line = background image

# Rich markdown text
> here.
```

## Quickstart
First, clone this repository. Then, proceed.
### config.json
Change the values in `config.json` to match your blog.
```json
{
    "name": "NAME",
    "tagline": "TAGLINE, could include HTML",
    "cta": ["LINK TEXT", "LINK HREF"]
}
```
The `cta` field defines the call to action link that will be in the hero section of your home page.
### raws/
The only other place you have to touch to get started is the `raws/` directory. Under `raws/`, add a directory. The name of this directory should be the name of a category of your blog. For example, you might create a directory `raws/Desserts` if you were working on a recipe website.

Under this inner directory, add a file ending in `.featured.imp`. The pre-suffix name of this file isn't important.

Fill the file with as explained above in the `.imp` section.

The `.featured` in the file extension tells Imp that this is the featured article for a category. Every category must have a featured article.
### Compile
Then, push your repository to GitHub. The actions workflow under `.github/` should compile the raws into their correct HTML format.  

If you don't use GitHub or you want to preview before pushing, install `requirements.txt` with pip and run `python compile.py`.

## License
This software is licensed under the Bok Choy General Software License. The full text of the license should be included below. If not, more information can be found at https://www.rockwill.dev/Bok-Choy-License/.
```
Bok Choy General Software License

Copyright (c) 2024 William Choi-Kim

This software and associated files (the "Software") may be used commercially, privately, and publicly. The Software may be modified in any way, without limitation. It may be distributed free of charge as is, but not distributed commerically without modifications to its functionality. Any distributed version of the Software must provide attribution to the Software in some way. Any distributed copy of the Software must abide by and include this license. The user is free to use, modify, and distribute the software under the aforementioned conditions.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```