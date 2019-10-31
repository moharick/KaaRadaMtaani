from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^mtaa/(\d+)', views.mtaa, name='mtaa'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^add_biz/', views.add_biz, name='add_biz'),
    url(r'^search/', views.search, name='search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
