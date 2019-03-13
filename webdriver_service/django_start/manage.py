#!/usr/bin/env python
import sys
import os

from django.http import HttpResponse

sys.path.append("../../")  # 解决潜在的路径依赖问题
sys.path.append("/root/scrapy-demo-beyebe")  # 解决潜在的路径依赖问题

def hello(request):
    return HttpResponse("Hello world ! ")

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_start.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)