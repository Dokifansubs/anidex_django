"""
WSGI config for anidex_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

try:
    import pymysql
    from gevent import monkey
    pymysql.install_as_MySQLdb()
    monkey.patch_all()
except ImportError as e:
    print e


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "anidex_django.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
