"""
Core urls
"""
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django_otp.admin import OTPAdminSite

admin.site.__class__ = OTPAdminSite
admin.site.site_header = "Personal Website Administration"
admin.site.site_title = "Personal Website Administration"

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += i18n_patterns(
    path('', include('apps.frontpage.urls', namespace='frontpage')),
    path(_('journal/'), include('apps.journal.urls', namespace='journal')),
    path(_('projects/'), include('apps.projects.urls', namespace='projects')),
    path(_('software/'), include('apps.software.urls', namespace='software')),
    path(_('articles/'), include('apps.articles.urls', namespace='articles')),
    path(_('quantified-self/'), include('apps.quantified_self.urls', namespace='quantified_self')),
    path('administration/', admin.site.urls),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
