"""
WSGI config for brd_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'django.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brd_site.settings')

application = get_wsgi_application()
