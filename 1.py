from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# 简历数据 - 根据您的实际情况修改
RESUME_DATA = {
    'name': '张三',
    'title': '全栈开发工程师',
    'contact': {
        'email': 'your.email@example.com',
        'phone': '+86 138-XXXX-XXXX',
        'github': 'github.com/yourusername',
        'linkedin': 'linkedin.com/in/yourprofile'
    },
    'about': '5年全栈开发经验，精通Python和JavaScript，有丰富的Web应用开发经验。',
    'experience': [
        {
            'company': 'ABC科技有限公司',
            'position': '高级开发工程师',
            'duration': '2020年6月 - 至今',
            'description': '负责公司核心产品的后端架构设计和开发，带领3人小组完成多个重要功能模块。'
        },
        {
            'company': 'XYZ软件公司',
            'position': 'Web开发工程师',
            'duration': '2018年3月 - 2020年5月',
            'description': '参与公司多个客户项目的全栈开发，主要使用Django和React技术栈。'
        }
    ],
    'education': [
        {
            'institution': '某某大学',
            'degree': '计算机科学与技术 硕士',
            'year': '2018'
        },
        {
            'institution': '某某大学',
            'degree': '软件工程 学士',
            'year': '2015'
        }
    ],
    'skills': [
        {'category': '编程语言', 'items': ['Python', 'JavaScript', 'Java']},
        {'category': 'Web框架', 'items': ['Flask', 'Django', 'React']},
        {'category': '数据库', 'items': ['MySQL', 'PostgreSQL', 'MongoDB']}
    ],
    'projects': [
        {
            'name': '在线教育平台',
            'description': '一个基于微服务的在线学习系统，支持视频课程、在线测试和证书发放。',
            'technologies': ['Python', 'Django', 'React', 'Docker']
        },
        {
            'name': '电商数据分析系统',
            'description': '为某电商公司开发的数据分析平台，提供销售预测和用户行为分析功能。',
            'technologies': ['Python', 'Pandas', 'Matplotlib', 'Flask']
        }
    ]
}

@app.route('/')
def resume():
    return render_template('resume.html', resume=RESUME_DATA)

@app.route('/download')
def download_resume():
    # 如果您有PDF版本简历，可以放在static文件夹并通过此路由提供下载
    return send_from_directory('static', 'resume.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)