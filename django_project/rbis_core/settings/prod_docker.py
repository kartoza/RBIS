
"""Configuration for production server"""
# noinspection PyUnresolvedReferences
try:
    from core.settings.prod_docker import *
    from rbis_core.settings.rbis import *  # noqa
except ImportError:
    pass

EMAIL_SUBJECT_PREFIX = '[RBIS]'
