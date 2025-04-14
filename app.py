from flask import Flask, render_template

app = Flask(__name__)

RESUME_DATA = {
    'name': 'Huang',
    'title': 'Python开发工程师',
    'years_experience': '300年',
    'contact': {
        'phone': '18888888888',
        'email': 'huangzihao289@gmail.com',
        'github': 'github.com/ua-Huang'
    },
    'skills': [
        'Python (Flask/Django)',
        'HTML/CSS/JavaScript',
        '数据库 (MySQL/PostgreSQL)',
        'Linux/Shell'
    ],
    'experience': [{
        'company': 'ABC科技有限公司',
        'position': 'Python开发工程师',
        'duration': '2020年1月 - 至今',
        'responsibilities': [
            '负责公司核心产品的后端开发',
            '优化系统性能，提升30%响应速度',
            '带领3人小组完成XX项目'
        ]
    }],
    'education': {
        'institution': 'XX大学',
        'major': '计算机科学与技术',
        'degree': '本科',
        'years': '2016-2020'
    },
    'projects': [{
        'name': '个人博客系统',
        'description': '基于Flask开发的个人博客系统，实现了用户认证、文章发布、评论等功能。'
    }]
}

@app.route('/')
def home():
    return render_template('index.html', resume=RESUME_DATA)

if __name__ == '__main__':
    app.run(debug=True)