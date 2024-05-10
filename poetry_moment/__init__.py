from flask import Blueprint, render_template_string

# 定义蓝图
poetry_moment_blueprint = Blueprint('poetry_moment', __name__, url_prefix='/poetry-moment')

# 插件的文档内容
poetry_moment_blueprint.docs = """
<h2>诗歌时刻</h2>
<p>让诗意，流露此刻。诗歌时刻是一款开源的API软件。他能帮助开发者简单快速的在网站/应用中嵌入诗歌。</p>
"""

main = poetry_moment_blueprint

@main.route('/')
def index():
    return "欢迎使用诗歌时刻！"