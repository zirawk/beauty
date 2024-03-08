import os
from pathlib import Path

USERNAME = 'songeating'
REPO = 'beauty'
BASEURL = f'https://mirror.ghproxy.com/https://raw.githubusercontent.com/{USERNAME}/{REPO}/master/flt/'
REPO_URL = f'https://github.com/{USERNAME}/{REPO}'


def gpages(base):
    mainpage_body = ''
    # Mark the left collection
    is_left = True
    tmp_left = ''
    # Every directory is a collection of images
    for dir in os.listdir(base):
        dir_path = os.path.join(base, dir)
        Path(dir).mkdir(parents=True, exist_ok=True)
        subpage_body = ''
        # Mark the first image
        first = True
        for root, ds, fs in os.walk(dir_path):
            # Every 'f' is an image
            for f in fs:
                img_src = BASEURL + os.path.join(dir, f)
                subpage_body += f'<img src="{img_src}">'
                # Use the first image as the cover of the collection
                if first:
                    first = False
                    sub_url = f'https://{USERNAME}.github.io/{REPO}/{dir}'
                    collection = f'<a href="{sub_url}"><div class="collection"><img class="cover" src="{img_src}"><p>{dir}</p></div></a>'
                    if is_left:
                        is_left = False
                        tmp_left = collection
                    else:
                        is_left = True
                        # Add collection to mainpage_body
                        mainpage_body += f'<div class="row">{tmp_left}{collection}</div>'
        # Generate subpage
        subpage_html = f'''<html>
<head>
<title>{dir}</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
<style>
* {{
    font-family: Helvetica, Arial, "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
}}
img {{
    width: 100%;
}}
</style>
</head>
<body>
<h1>{dir}</h1>
{subpage_body}
</body>
</html>'''
        open(os.path.join(dir, 'index.html'), 'w').write(subpage_html)
    # Generate mainpage
    mainpage_html = f'''<html>
<head>
<title>Beauty</title>
<p>GitHub: <a href="{REPO_URL}">{USERNAME}/{REPO}</a></p>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
<style>
* {{
    font-family: Helvetica, Arial, "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
}}
img.cover {{
    width: 100%;
}}
div.collection {{
    display: inline-block;
    width: 50%;
}}
div.row a {{
    text-decoration: none;
    color: inherit;
}}
</style>
</head>
<body>
<h1>Beauty</h1>
{mainpage_body}
</body>
</html>'''
    open('index.html', 'w').write(mainpage_html)


base = './flt'
gpages(base)
