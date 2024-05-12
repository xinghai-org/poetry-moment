from apicat import config
def docs():
    html = """
<h2>诗歌时刻<h2>
<h3>简介</h3>
让诗意，流露此刻。诗歌时刻是一款基于APICat的API软件。他能帮助开发者简单快速的，在网站/应用中嵌入诗歌。
<h3>使用<h3>
<h4>以返回数据解析（GET请求）<h4>
<p>
    纯文本返回："""+config.get_website_url()+"""/poetry-moment/get/text<br>
    JSON返回："""+config.get_website_url()+"""/poetry-moment/get/json
</p>
    """
    return html