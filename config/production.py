import os
import dj_database_url
from .settings import *

DATABASES = {
    'defalut' : dj_database_url.config()
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'