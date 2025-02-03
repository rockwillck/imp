import os
from markdown2 import markdown
import shutil
import json

with open("config.json",'r') as c:
	conf = json.loads(c.read())
name = conf["name"]
tagline = conf["tagline"]
homecta = conf["cta"]
navOrder = conf["nav"]

subs = {}
dirs = sorted(os.listdir('raws')) if len(navOrder) == 0 else navOrder
navDiv = "\n".join(map(lambda a : f'<a href="../{a}/index.html">{a}</a>',dirs))
for dir in dirs:
    try:
        shutil.rmtree(dir)
    except:
        pass
    os.mkdir(dir)
    allArt = []
    featured = []
    for f in sorted(os.listdir(f'raws/{dir}')):
        with open(f'raws/{dir}/{f}', 'r') as cont:
            lines = cont.readlines()
            title = lines[0].strip()
            sub = lines[1].strip()
            bg = lines[2]
            md = "  \n".join(list(map(lambda x : x.strip(), lines[3:]))).strip()

            artCont = f'''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<title>{title} | {name}</title>
	<meta name="viewport" content="width=device-width,initial-scale=1" />
	<meta name="description" content="{sub}" />
	<link rel="stylesheet" type="text/css" href="../style.css" />
    <link rel="stylesheet" type="text/css" href="../article.css" />
	<link rel="icon" href="../assets/icon.svg">
</head>
<body>
	<div class="site">
		<div class="nav">
			<h1><a href="/">{name}</a></h1>
            {navDiv}
		</div>
        <div class="content">
            <div class="header" style="background-image:url({bg})"></div>
            <div>
                <h1>{title}</h1>
                <sub>{sub}</sub>
                {markdown(md)}
            </div>
        </div>
</body>
</html>'''

            if ".featured" in f:
                featured = [title, sub, bg, f.split(".")[0]]
            else:
                allArt.append([title, sub, bg, f.split(".")[0]])

            base = f.split('.')[0]
            with open(f'{dir}/{base + ".html"}', 'w') as tbw:
                tbw.write(artCont)
    subs[dir] = [featured, allArt]

            
featuredDivs = []
for dir in subs.keys():
    data = subs[dir]
    featured = data[0]
    ee = data[1]
    featuredDivs.append([featured, dir])
    indexFile = f'''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<title>{dir}</title>
	<meta name="viewport" content="width=device-width,initial-scale=1" />
	<meta name="description" content="{tagline}" />
	<link rel="stylesheet" type="text/css" href="../style.css" />
	<link rel="icon" href="../assets/icon.svg">
</head>
<body>
	<div class="site">
		<div class="nav">
			<h1><a href="/">{name}</a></h1>
            {navDiv}
		</div>
		<div class="banner" id="banner" data-bg="{featured[2]}">
			<div class="caption">
				<h1>{featured[0]}</h1>
				<sub>{featured[1]}</sub>
				<a class="cta" href="{featured[3]}.html">Read</a>
			</div>
		</div>
		<div class="cards">
            {
                "\n".join(map(
                    lambda b : f'''
			<div class="card" id="card1" data-bg="{b[2]}">
				<a class="cardLink" href="{b[3]}.html">
					<h2>{b[0]}</h2>
					<sub>{b[1]}</sub>
				</a>
			</div>'''
                    , ee
                ))
            }
		</div>
	</div>
	<script src="../app.js"></script>
</body>
</html>'''
    with open(f'{dir}/index.html', 'w') as inw:
        inw.write(indexFile)

with open('index.html', 'w') as homepage:
    homepage.write(f'''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<title>{name}</title>
	<meta name="viewport" content="width=device-width,initial-scale=1" />
	<meta name="description" content="{tagline}" />
	<link rel="stylesheet" type="text/css" href="style.css" />
	<link rel="icon" href="assets/icon.svg">
</head>
<body>
	<div class="site">
		<div class="nav">
			<h1><a href="/">{name}</a></h1>
			{navDiv}
		</div>
		<div class="banner" id="banner" data-bg="assets/landing.png">
			<div class="caption">
				<h1>{name}</h1>
				<sub>{tagline}</sub>
				<a class="cta" href="{homecta[1]}">{homecta[0]}</a>
			</div>
		</div>
		<div class="cards">
			{
                "\n".join(map(
                    lambda b : f'''
			<div class="card" id="card1" data-bg="{b[0][2]}">
				<a class="cardLink" href="{b[1]}/{b[0][3]}.html">
                    <small>{b[1]}/</small>
					<h2>{b[0][0]}</h2>
					<sub>{b[0][1]}</sub>
				</a>
			</div>'''
                    , featuredDivs
                ))
            }
		</div>
	</div>
	<script src="app.js"></script>
</body>
</html>''')