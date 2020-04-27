from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return """
    <h1>Миссия Колонизация Марса </h1>
    """


@app.route('/index')
def index():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route('/promotion')
def promotion():
    return """
    <p>Человечество вырастает из детства. </p>
    <p>Человечеству мала одна планета. </p>
    <p>Мы сделаем обитаемыми безжизненные пока планеты. </p>
    <p>И начнем с Марса! </p>
    <p>Присоединяйся! </p>
    """


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс! </h1>
                    <img src="/static/mars.jpg">
                    <p>Вот она какая, красная планета </p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
