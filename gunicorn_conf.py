wsgi_app = 'application:app'
bind = '0.0.0.0:80'
worker_class = 'sync'
accesslog = '/logs/rsted_access.log'
acceslogformat ="%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"
errorlog =  '/logs/rsted_error.log'
disable_redirect_access_to_syslog = True
preload_app = True

