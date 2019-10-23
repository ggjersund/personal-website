"""
Core urls
"""
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django_otp.admin import OTPAdminSite

from . views import frontpage

admin.site.__class__ = OTPAdminSite
admin.site.site_header = "Personal Website Administration"
admin.site.site_title = "Personal Website Administration"

urlpatterns = []

urlpatterns += i18n_patterns(
    path('', frontpage, name='frontpage'),
    path('administration/', admin.site.urls),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
