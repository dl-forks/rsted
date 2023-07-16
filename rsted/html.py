
import os
import sys
from os.path import join as J
#import codecs

from docutils.core import publish_string

#utf8codec = codecs.lookup('utf-8')

# see http://docutils.sourceforge.net/docs/user/config.html
default_rst_opts = {
    'no_generator': True,
    'no_source_link': True,
    'tab_width': 4,
    'file_insertion_enabled': False,
    'raw_enabled': False,
    'stylesheet_path': None,
    'traceback': True,
    'halt_level': 5,
    'embed_stylesheet': False,
    "syntax_highlight": "short",
}


def rst2html(rst, css_path_prefix: str = None, theme=None, opts=None):
    rst_opts = default_rst_opts.copy()
    if opts:
        rst_opts.update(opts)
    rst_opts['template'] = 'var/themes/template.txt'

    stylesheets = ["basic.css"]
    if theme:
        stylesheets.append(f"{theme}.css")
    if css_path_prefix:
        rst_opts["stylesheet_path"] = ",".join([J(css_path_prefix, p) for p in stylesheets]+"css/syntax.css")
    else:
        rst_opts["stylesheet_path"] = "css/syntax.css"

    out = publish_string(rst, writer_name="html", settings_overrides=rst_opts)

    return out
