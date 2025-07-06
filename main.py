import json
from jinja2 import Environment, FileSystemLoader

# 读取JSON
with open('data1to25.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

cases = data['1to25']['案件列表']

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('case_side.html')

for case in cases:
    case_num = case.get('案件序号', 'unknown')
    html = template.render(case=case)
    with open(f'./murdle_htmls/case_{case_num}.html', 'w', encoding='utf-8') as f:
        f.write(html)

# 新增渲染首页（index.html）
# 选取第一个案件为首页内容示例（可根据需要调整）
if cases:
    index_html = template.render(case=cases[0])
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)

print("所有案件HTML及首页已生成。")