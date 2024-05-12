# 导入所需模块
from apicat import config
import os
import json
import random
import time

plugin_name = 'poetry_moment'
directory = config.get_plugin_cfg(plugin_name,"directory")

def get():
    # 获取该目录下所有文件的列表
    json_files = [file for file in os.listdir(directory) if file.endswith('.json')]
    # 随机选择一个语录文件
    discourse_file = random.choice(json_files)
    # 打开并读取所选文件的内容，将其解析为JSON对象
    with open(os.path.join(directory, discourse_file), 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
        # 随机选择一个语录数据项
        selected_data = random.choice(data)
        # 构建返回结果字典，包含状态、消息、类别、内容、来源、收录者和日期信息
        final_data = {
            'status': '200',
            'msg': '成功',
            'category': os.path.splitext(discourse_file)[0],
            'content': selected_data.get('content'),
            'from': selected_data.get('from'),
            'creator': selected_data.get('creator'),
            'date': selected_data.get('date')
        }
    # 返回构建好的对话数据字典
    return final_data


def post(content, category, user):
    # 创建待写入的新语录记录字典
    new_entry = {
        "content": content,
        "from": "user",
        "creator": user,
        "date": time.strftime("%Y-%m-%d", time.localtime())
    }
    new_filename = f"{category}.json"
    # 写入新语录
    with open(os.path.join(directory, new_filename), 'w+', encoding='utf-8') as file:
        json.dump(new_entry, file, ensure_ascii=False, indent=4)
    # 返回新创建语录的详细信息
    poetry_data = {
        'status': '200',
        'msg': '创建成功！',
        'category': category,
        'content': content,
        'creator': user,
        'date': time.strftime("%Y-%m-%d", time.localtime())
    }
    return poetry_data