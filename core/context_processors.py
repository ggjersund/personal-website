"""
Context processors
"""
from django.conf import settings


def from_settings(request):
    """
    Set context variables based on settings variables
    """
    return {
        'ENVIRONMENT_NAME': settings.ENVIRONMENT_NAME,
        'ENVIRONMENT_COLOR': settings.ENVIRONMENT_COLOR,
    }
