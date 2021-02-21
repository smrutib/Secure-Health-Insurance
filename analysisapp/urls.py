from django.urls import path
from analysisapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.splash),
    path('index', views.index),
    path('provider', views.provider),
    path('charts/', views.charts),
    path('charts2/', views.charts2),
    path('start', views.start),
    path('Maps', views.Maps),
    path('table', views.table),
    path('form', views.fileforms),
    path('submit', views.submit_claim)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)