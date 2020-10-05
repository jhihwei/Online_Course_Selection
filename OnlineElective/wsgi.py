"""
WSGI config for OnlineElective project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dj_static import Cling # <- 加入
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineElective.settings')

# application = get_wsgi_application()
application = Cling(get_wsgi_application())
