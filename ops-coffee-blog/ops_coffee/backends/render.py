import os
from jinja2 import Template
from markdown import markdown
from django.conf import settings
from ops_coffee.models import Blog
from ops_coffee.backends.gitpush import GitRun

tmpl = """<!DOCTYPE html>
<html lang="zh-CN">

<head>
  <meta name="theme-color" content="#2879d0" />
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="copyright" content="©2018 运维咖啡吧版权所有 ops-coffee.cn" />
  <link rel="stylesheet" href="/css/style.min.css" media="screen" type="text/css" />

  <!-- Begin SEO tag -->
  <title>{{ title }}</title>
  <meta property="og:locale" content="zh_CN" />
  <meta property="og:title" content="{{ title }}" />
  <meta property="og:description" content="{{ description }}" />
  <meta name="description" content="{{ description }}" />
  <link rel="canonical" href="https://ops-coffee.cn/" />
  <meta property="og:url" content="https://ops-coffee.cn/" />
  <meta property="og:site_name" content="运维咖啡吧" />
  <!-- End SEO tag -->
</head>

<body>
  <header>
    <div class="inner">
      <a href="https://ops-coffee.cn/">
        <h1>运维咖啡吧</h1>
      </a>
      <h2>追求技术的道路上，我从不曾停下脚步</h2>
    </div>
  </header>

  <div id="content-wrapper">
    <div class="inner clearfix">
      <section id="main-content">
      {% if havet %}
        <h1 id="art-title">{{ title }}</h1>
      {% endif %}
      
      {{ content }}
      </section>

      <aside id="sidebar">
        <blockquote class="route">微信公众号</blockquote>
        <img border="0" src="/images/z-qrcode.jpg" width="100%" height="100%" alt="ops-coffee" />

        <blockquote class="route">归档列表</blockquote>
        <div class="sidebar-list"><a href="/"> 精选文章列表</a></div>
        <div class="sidebar-list"><a href="/s/"> 日常运维记录</a></div>
      </aside>
    </div>

    <footer>
      <div id="site-footer">
        <div style="float:left">
          © 2019 <span title="ops-coffee">ops-coffee</span>
        </div>

        <ul id="site-footer-links" style="float:right">
          <li>
            <a href="#sidebar" onclick="if(confirm('扫描二维码，关注有惊喜')==false)return false;" title="关于本站" target="">关于本站</a>
          </li>
          <li>
            <a href="#sidebar" onclick="if(confirm('扫描二维码，关注有惊喜')==false)return false;" title="友情链接" target="">友情链接</a>
          </li>
        </ul>
      </div>
    </footer>
  </div>

  <script type="text/javascript">
    var _hmt = _hmt || [];
    (function () {
      var hm = document.createElement("script");
      hm.src = "https://hm.baidu.com/hm.js?84eb0bf97b63c13ada0074cb12a49b71";
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(hm, s);
    })();
  </script>
</body>

</html>
"""


class RenderHtml:
    def __init__(self):
        self.blogDir = settings.OPS_COFFEE_GIT_DIR

    def index(self, content):
        kwargs = {
            "havet": 0,
            "title": "运维咖啡吧",
            "description": "追求技术的道路上，我从不曾停下脚步",
            "content": content
        }

        try:
            _content = Template(tmpl).render(kwargs)

            with open(self.blogDir + '/index.html', 'w', encoding='utf8') as f:
                f.write(_content)

            state, data = GitRun().push()
            if state:
                return True, '上传Git成功 ^_^'
            else:
                return False, '上传Git失败 ~_~'
        except Exception as e:
            return False, str(e)

    def detail(self, id):
        _blog = Blog.objects.get(id=id)

        if not os.path.isdir(self.blogDir + '/' + _blog.path.strip()):
            os.mkdir(self.blogDir + '/' + _blog.path.strip())

        kwargs = {
            "havet": 1,
            "title": _blog.title,
            "description": _blog.title,
            "content": markdown(_blog.content,
                                extensions=['extra', 'codehilite', 'tables', 'toc'])
        }

        try:
            _content = Template(tmpl).render(kwargs)

            file = self.blogDir + '/' + _blog.path.strip() + '/' + _blog.name.strip() + '.html'
            with open(file, 'w', encoding='utf8') as f:
                return True, f.write(_content)

        except Exception as e:
            return False, str(e)

    def blogs(self):
        _list = Blog.objects.filter(is_deleted=0)
        success, pathdic = 0, {}

        for i in _list:
            state, dt = RenderHtml().detail(i.id)

            # 如果生成成功
            if state:
                success += 1

                pathdic.setdefault(i.path.strip(), []).append({i.name.strip(): i.title})

        # 生成对应的index.html页
        data = {"total": _list.count(), "success": success}
        for path, blogs in pathdic.items():
            content = '<ul>\n'
            for i in blogs:
                for name, title in i.items():
                    content += '<li><a href="/%s/%s.html" target="_blank" rel="noreferrer">%s</a></li>\n' % (
                        path.strip(), name.strip(), title
                    )

            kwargs = {
                "havet": 0,
                "title": "运维咖啡吧",
                "description": "追求技术的道路上，我从不曾停下脚步",
                "content": content + '</ul>'
            }

            try:
                _content = Template(tmpl).render(kwargs)

                with open(self.blogDir + '/%s/index.html' % path.strip(), 'w', encoding='utf8') as f:
                    f.write(_content)

                state, dt = GitRun().push()
                data['git'] = '上传Git成功 ^_^' if state else '上传Git失败 ~_~'

                return state, data
            except Exception as e:
                return False, str(e)
