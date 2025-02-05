# Beauty

<https://zirawk.github.io/beauty>

## 本Fork

将镜像站网址更新为未被墙的<ghfast.top>

另外，<fulitu.me>似乎不再提供服务，故本repo不再增加新写真（大概）

## 起因

<https://fulitu.me>的写真，每页只显示三张图片，且有很多广告。
于是我写了个简单的Python脚本，批量下载一个图集中的图片。
截止到本次commit，共有114个图集，6547张图片（如果我没搞错的话）。
由此也有了部署到GitHub Pages的想法，于是又写了个Python脚本，生成html文件。

由于没怎么学过html，Python也没学过多少，代码大多是现查现学的，
所以网页写的并不美观，脚本可能也有一些问题，勿喷。

## 关于图片

只选取了符合我xp的图片，不一定符合你的。
（我的xp大致是：jk制服，贫乳，白丝，白丝，白丝）

图集的名称是<https://fulitu.me>上的原名，未做修改。个别图集名与实际内容并不相符。

其中*桃良阿宅 - 唤醒 40P*和*[Yoko宅夏]妹汤物语-校服 63P*
两个图集的图源是<https://xx.knit.bid>，为手动下载。

## 关于Python脚本

如果你需要使用我写的脚本，那么这是一个说明。

### 安装依赖：

```bash
pip install requests beautifulsoup4
```

### flt.py

`flt.py`用于从<https://fulitu.me>下载一个图集中的全部图片。
根据你的实际情况将`save_dir`设置为保存目录。

进入<https://fulitu.me>上的一个图集，复制其第一页的网址，运行命令：

```bash
python flt.py <网址>
```

将开始递归下载每一页的图片，并保存在`${save_dir}/<图集名>`下。

如果你进入其他页码，请切换回第一页，否则先前页码的图片将不会被下载。

### generate.py

`generate.py`用于为每个图集生成部署到GitHub Pages的html文件。
将`USERNAME`和`REPO`修改为你自己的，将`base`修改为存放图集文件夹的目录，
相当于`flt.py`中的`save_dir`。

然后直接运行命令：

```bash
python generate.py
```

生成的html中的img会使用<https://mirror.ghproxy.com>代理以加速中国大陆地区访问。
如果你不需要，可以自行修改。

### 已知的问题

`flt.py`下载图片时，每一页的第一张图片会下载两次。
但<https://fulitu.me>确实把每一页的第一张图片的img标签写了两次。

如果在下载中途中断，脚本将终止，需要重新运行命令。

如果你有能力，我还是建议你自己写。这两个脚本只是我为解决临时需求现学现写的。
