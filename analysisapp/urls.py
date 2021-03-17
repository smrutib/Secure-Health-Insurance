from django.urls import path
from analysisapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'analysisapp'

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
    path('submit', views.submit_claim, name='submit'),
    path('status',views.status, name='status'),
    path('docver/<int:i>/', views.docver, name='docver'),
    path('docverdone/<int:i>/', views.docverdone, name='docverdone'),
    path('claimapprove', views.claimapprove, name='claimapprove'),
    path('approval/<int:i>/<str:s>/', views.approval, name='approval'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)