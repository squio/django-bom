from django.conf import settings  # import the settings file


def bom_config(request):
    base_template = 'bom/base.html'
    app_name = 'IndaBOM'
    if settings.BOM_CONFIG:
        if 'base_template' in settings.BOM_CONFIG:
            base_template = settings.BOM_CONFIG['base_template']
        if 'app_name' in settings.BOM_CONFIG:
            app_name = settings.BOM_CONFIG['app_name']
    return {
        'BASE_TEMPLATE': base_template,
        'APP_NAME': app_name,
    }
