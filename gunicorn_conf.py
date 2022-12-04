wsgi_app = 'application:app'
bind = '0.0.0.0:80'
worker_class = 'sync'
errorlog =  '/logs/rsted_error.log'
accesslog = '/logs/rsted_access.log'
access_log_format ='%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(M)sms'
disable_redirect_access_to_syslog = True
preload_app = True




# ==============  ========================================
#       h         remote address
#       l         '-'
#       u         user name
#       t         date of the request
#       r         status line (e.g. GET / HTTP/1.1)
#       m         request method
#       U         URL path without query string
#       q         query string
#       H         protocol
#       s         status
#       B         response length
#       b         response length or '-' (CLF format)
#       f         referer
#       a         user agent
#       T         request time in seconds
#       M         request time in milliseconds
#       D         request time in microseconds
#       L         request time in decimal seconds
#       p         process ID
#  {header}i      request header
#  {header}o      response header
#  {variable}e    environment variable
# ==============  ========================================
#
# https://docs.gunicorn.org/en/stable/settings.html
