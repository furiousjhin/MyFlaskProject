from flask import Flask
import random

app = Flask(__name__)


# 일반적인 웹프레임워크에서 이런 데이터들은 데이터베이스에 저장하게된다.
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]


def template(contents, content):
    return f'''
        <!doctype html>
        <html>

            <head>
            </head>

            <body>
                <h1><a href="/">WEB</a></h1>
                <ol>
                    {contents}
                </ol>
                {content}
            </body>
            <ul>
                <li><a href="/create/">create</a></li>
            </ul>
        </html>
    '''


def get_contents():
    li_tags = ''
    for topic in topics:
        li_tags = li_tags + f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'

    return li_tags


@app.route('/')
def index():
    return template(get_contents(), '<h2>Welcome</h2>')


@app.route('/create/')
def create():
    return template(get_contents(), 'create')


# 라우팅 할 때 변수를 받기 위해서는 <변수> 를 통해서 받는다.
# <> 안에 '자료형:'을 적어주면 자동으로 해당 자료형으로 받는다.
@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''

    if len(topics) >= id >= 1:
        title = title + f'{topics[id - 1]["title"]}'
        body = body + f'{topics[id - 1]["body"]}'
    else:
        title = title + '올바른 경로가 아닙니다.'
        body = body + '돌아가세요.'

    return template(get_contents(), f'<h2>{title}</h2><p>{body}</p>')


app.run(port=5000, debug=True)