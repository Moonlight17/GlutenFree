# coding=utf-8
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('<int:count>/', views.ListRecept.as_view(), name='ListRecept'),
    path('tag/', views.TagLoad.as_view(), name='TagLoad'),
    path('recept/<int:id>/', views.ListCurrentRecept.as_view(), name='ListCurrentRecept'),
    path('add/', views.AddRecept.as_view(), name='add'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

