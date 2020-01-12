"""
WSGI config for CVParser project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CVParser.settings')


# hack for downloading packages each time heroku restart service
if os.environ.get('HEROKU_ENV', None):
    import spacy.cli
    from nltk.downloader import download as ntlk_download
    ntlk_path = os.path.join(settings.BASE_DIR, 'ntlk_data')
    spacy.cli.download('en_core_web_sm')
    ntlk_download('words', download_dir=ntlk_path)
    ntlk_download('stopwords', download_dir=ntlk_path)


application = get_wsgi_application()
