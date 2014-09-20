#!/usr/bin/env python
try:
    import pymysql
    from gevent import monkey
    pymysql.install_as_MySQLdb()
    monkey.patch_all()
except ImportError as e:
    print e


import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "anidex_django.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
