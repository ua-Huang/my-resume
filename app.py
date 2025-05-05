from flask import Flask, render_template

app = Flask(__name__)

RESUME_DATA = {
    'name': '黄梓豪',
    'title': 'Python开发工程师',
    'years_experience': '超级多年',
    'contact': {
        'phone': '188888888888',
        'email': ':huangzihao289@gmail.com',
        'github': 'github.com/ua-Huang'
    },
    'skills': [
        'Python (Flask/Django)',
        'HTML/CSS/JavaScript',
        '数据库 (MySQL/PostgreSQL)',
        'Linux/Shell',
        '通信专业户'
    ],
    'experience': [{
        'company': '嘉黎顿梦想公司',
        'position': 'Python开发工程师',
        'duration': '2022年1月 - 至今',
        'responsibilities': [
            '参与公司核心项目的开发与维护',
            '协助团队完成需求分析和功能设计',
            '负责部分模块的代码编写和测试'
        ]
    }],
    'education': {
        'institution': '北方民族大学',
        'major': '电子信息工程',
        'degree': '本科',
        'years': '2022-2026'
    },
    'projects': [{
        'name': 'ai智能问答系统',
        'description': '使用Python和自然语言处理技术开发的智能问答系统，能够回答特定领域的问题'
    }]
}


@app.route('/')
def home():
    return render_template('index.html', resume=RESUME_DATA)  # 确保返回的是模板渲染结果


if __name__ == '__main__':
    app.run(debug=True)
    # 生成静态 HTML
    with app.test_request_context():
        rendered_html = render_template('index.html', resume=RESUME_DATA)

        # 替换 url_for 路径为相对路径
    rendered_html = rendered_html.replace('static/images/profile.jpg', 'static/images/profile.jpg')
    rendered_html = rendered_html.replace('/static/images/profile.jpg', 'static/images/profile.jpg')

    # 保存到 index.html
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(rendered_html)
