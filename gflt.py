import os

USERNAME = 'songeating'
REPO = 'beauty'
BASEURL = f'https://mirror.ghproxy.com/https://raw.githubusercontent.com/{USERNAME}/{REPO}/master/flt/'
REPO_URL = f'https://github.com/{USERNAME}/{REPO}'


def gpages(base):
    mainpage_body = ''
    # Every directory is a collection of images
    for dir in os.listdir(base):
        dir_path = os.path.join(base, dir)
        os.mkdir(dir)
        subpage_body = ''
        # Mark the first image
        first = True
        for root, ds, fs in os.walk(dir_path):
            # Every 'f' is an image
            for f in fs:
                img_src = BASEURL + os.path.join(dir, f)
                subpage_body += f'<img src="{img_src}">'
                if first:
                    first = False
                    # Add collection to mainpage_body
                    sub_url = f'https://{USERNAME}.github.io/{REPO}/dir'
                    mainpage_body += f'<a href="{sub_url}"><div><img class="cover" src="{img_src}"><div>{dir}</div></div></a><br><br>'
        # Generate subpage
        subpage_html = f'''<html>
<head>
<title>{dir}</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
<style>
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
img.cover {{
    width: 100%;
}}
</style>
</head>
<body>
<h1>Beauty</h1>
{mainpage_body}
</body>
</html>'''
    open('index.html', 'w').write(mainpage_html)


#base = '/sdcard/Download/flt'
base = './flt'
gpages(base)
