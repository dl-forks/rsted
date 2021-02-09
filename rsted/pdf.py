import sys
from rst2pdf.createpdf import RstToPdf
import codecs
utf8codec = codecs.lookup('utf-8')

from flask import current_app

if sys.version_info > (3,):
    #from io import StringIO
    from io import BytesIO
else:
    try:
        from cStringIO import StringIO as BytesIO
    except ImportError:
        from StringIO import StringIO as BytesIO

def rst2pdf(content, theme=None):
    topdf = RstToPdf(basedir=current_app.config.root_path, breaklevel=0)
    buf = BytesIO()

    if not content:
        content = '\0'
    content_utf8 = utf8codec.encode(content)[0]
    topdf.createPdf(text=content_utf8, output=buf, compressed=False)

    return buf.getvalue()
