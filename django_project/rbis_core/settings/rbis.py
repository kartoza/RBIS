try:
    from core.settings.contrib import TEMPLATES, STATICFILES_DIRS  # noqa
    from rbis_core.settings.utils import rbis_absolute_path
except ImportError:
    pass

try:
    TEMPLATES[0]['DIRS'] = [  # noqa
        rbis_absolute_path('rbis_core', 'base_templates'),
    ] + TEMPLATES[0]['DIRS']  # noqa
    # Additional locations of static files
    STATICFILES_DIRS = [
       rbis_absolute_path('rbis_core', 'base_static'),
    ] + STATICFILES_DIRS  # noqa
except (KeyError, NameError):
    pass
