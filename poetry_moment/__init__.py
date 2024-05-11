from flask import Blueprint, render_template_string, request, jsonify
from . import core
import xhlog as log

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

@main.route('/get/<poetry_type>')
def get_poetry(poetry_type):
    if poetry_type=='text':
        log.info(f"请求IP: {request.remote_addr} 请求内容: 文本")
        result = core.get()
        return result.get('content', 0), 200
    if poetry_type=='json':
        log.info(f"请求IP: {request.remote_addr} 请求内容: JSON")
        response_data = core.get()
        return jsonify(response_data), 200
    return "请求类型错误", 404

@main.route('/post')
def post_poetry():
    log.info(f"请求IP: {request.remote_addr} 请求内容: 提交")
    content = request.args.get('content', None)
    category = request.args.get('category', 'default')
    user = request.args.get('user', '雷锋')
    if content is None:
        return "无内容！", 404
    return jsonify(core.post(content, category, user)), 200