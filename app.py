from flask import Flask, render_template, request
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/param', methods=['GET', 'POST'])
def param():
    name = request.args.get('name')
    if name is None:
        name = request.form.get('name')
    return render_template('param.html', name=name)


if __name__ == '__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
    app.run()
