
from django.urls import include, path
from BAZAR import settings
from django.conf.urls.static import static

from admin_app import views

urlpatterns = [
    path("admin-home",views.AdminHomeView.as_view(), name="admin-home"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)