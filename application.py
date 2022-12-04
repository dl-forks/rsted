#!/usr/bin/env python3
# all the imports

import os, sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

from flask import Flask, request, render_template, make_response, url_for, Blueprint

from rsted.html import rst2html as _rst2html
from rsted.pdf import rst2pdf as _rst2pdf

from flaskext.helpers import render_html

# handle relative path references by changing to project directory
#run_from = os.path.dirname(os.path.abspath(sys.argv[0]))
#if run_from != os.path.curdir:
#    os.chdir(run_from)
# when running gunicorn, ^^ this only makes things worse

# create our little application :)

app = Flask(__name__, static_url_path='/rsted/static')
app.config.from_pyfile(os.environ.get("RSTED_CONF", "settings.py"))

bp = Blueprint(
    "rsted",
    __name__,
    url_prefix="/rsted"
)


def view_is_active(view_name):
    if request.path == url_for(view_name):
        return 'active'
    return ''

@bp.context_processor
def ctx_pro():
    return {
        'is_active': view_is_active,
    }

@bp.route("/")
@render_html('index.html')
def index():
    yield 'js_params', {'theme': request.args.get('theme', '')}


@bp.route('/rst2html/', methods=['POST', 'GET'])
def rst2html():
    rst = request.form.get('rst', '')
    theme = request.form.get('theme')
    if theme == 'basic':
        theme = None
    html = _rst2html(rst, theme=theme)
    return html

@bp.route('/rst2pdf/', methods=['POST'])
def rst2pdf():
    rst = request.form.get('rst', '')
    theme = request.form.get('theme')
    if theme == 'basic':
        theme = None

    pdf = _rst2pdf(rst, theme=theme)
    responce = make_response(pdf)
    responce.headers['Content-Type'] = 'application/pdf'
    responce.headers['Content-Disposition'] = 'attachment; filename="rst.pdf"'
    responce.headers['Content-Transfer-Encoding'] = 'binary'
    return responce


app.register_blueprint(bp)

import log
log.init()

if __name__ == '__main__':
    app.run(host=app.config.get('HOST', '0.0.0.0'),
            port=app.config.get('PORT', 5000))
