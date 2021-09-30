from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('account/', include('account.urls'), name = 'account'),
    path('account/', include('django.contrib.auth.urls')),
    path('myprofile/', include('myprofile.urls', namespace="myprofile")),
    path('merchant/', include('merchant_app.urls', namespace = 'merchant_app')),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

admin.site.site_header = 'New Age Shopping'
admin.sites.AdminSite.index_title = 'New Age Shopping'
admin.site.site_title = 'Admin Panel'