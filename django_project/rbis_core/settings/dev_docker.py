# -*- coding: utf-8 -*-
"""Settings for when running under docker in development mode."""
import os
try:
    from core.settings.dev_docker import *  # noqa
    from rbis_core.settings.rbis import *  # noqa
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gis',
        'USER': 'docker',
        'PASSWORD': 'docker',
        'HOST': 'db',
        'PORT': 5432,
        'TEST': {
            'NAME': 'gis_test'
        },
    }
}

if os.getenv('DEFAULT_BACKEND_DATASTORE'):
    DATABASES[os.getenv('DEFAULT_BACKEND_DATASTORE')] = {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geonode_data',
        'USER': 'geonode_data',
        'PASSWORD': 'docker',
        'HOST': 'geonode-db',
        'PORT': 5432
    }

OGC_SERVER_DEFAULT_USER = 'admin'
OGC_SERVER_DEFAULT_PASSWORD = 'admingeoserver'
DEFAULT_BACKEND_UPLOADER = 'geonode.rest'
