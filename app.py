from flask import Flask, render_template

app = Flask(__name__)

RESUME_DATA = {
    'name': 'Huang',
    'title': 'Python开发工程师',
    'years_experience': '很多年',
    'contact': {
        'phone': '18888888888',
        'email': 'huangzihao289@gmail.com',
        'github': 'github.com/ua-Huang'
    },
    'skills': [
        'Python (Flask/Django)',
        'HTML/CSS/JavaScript',
        '数据库 (MySQL/PostgreSQL)',
        'Linux/Shell',
        '数字图像处理'
    ],
    'experience': [{
        'company': 'ABC科技有限公司',
        'position': 'Python开发工程师',
        'duration': '2020年1月 - 至今',
        'responsibilities': [
            '负责公司核心产品的后端开发',
            '优化系统性能，提升30%响应速度',
            '带领2人小组完成简历项目'
        ]
    }],
    'education': {
        'institution': '北方民族大学',
        'major': '电子信息工程',
        'degree': '本科',
        'years': '2022-2026'
    },
    'projects': [{
        'name': '个人博客系统',
        'description': '基于Flask开发的个人博客系统，实现了用户认证、文章发布、评论等功能。'
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


    # 保存到 index.html
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(rendered_html)

    print("✅ 静态 HTML 已生成：index.html")