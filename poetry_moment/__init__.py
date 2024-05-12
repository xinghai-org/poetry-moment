from flask import Blueprint, render_template_string, request, jsonify
from . import core
import xhlog as log
from .docs import docs
from apicat import config

# 定义蓝图
blueprint = Blueprint('poetry_moment', __name__, url_prefix='/poetry-moment')

main = blueprint

@main.route('/')
def index():
    return render_template_string(docs())

@main.route('/get/<poetry_type>')
def get_poetry(poetry_type):
    content = core.get()
    if poetry_type=='text':
        log.info(f"请求IP: {request.remote_addr} 请求内容: 文本")
        return content.get('content', 0), content.get('status', 0)
    if poetry_type=='json':
        log.info(f"请求IP: {request.remote_addr} 请求内容: JSON")
        return jsonify(content), content.get('status', 0)
    if poetry_type=='card':
        log.info(f"请求IP: {request.remote_addr} 请求内容: 诗词卡片")
        card = f"""
<body>
{content.get('content', 0)}
<br>
————{content.get('from', 0)}
</body>
"""+"""
<style>
body {
    background-image: url(https://bing.shangzhenyang.com/api/1080p);
    background-size: cover;
}
</style>
"""
        return render_template_string(card), content.get('status', 0)
    else:
        return "请求类型错误", 404

@main.route('/post')
def post_poetry():
    log.info(f"请求IP: {request.remote_addr} 请求内容: 提交")
    content = request.args.get('content', None)
    token = request.args.get('token', "123456")
    category = request.args.get('category', 'default')
    user = request.args.get('user', '雷锋')
    if content is None:
        return "无内容！", 404
    elif token != config.get_plugin_cfg('poetry-moment', 'token', default="123456"):
        return "token错误！", 404
    content = core.post(content, category, user)
    return jsonify(content), content.get('status', 0)