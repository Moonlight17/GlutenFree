# coding=utf-8
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('<int:count>/', views.ListRecept.as_view(), name='ListRecept'),
    path('tag/', views.TagLoad.as_view(), name='TagLoad'),
    path('user/<int:id>/', views.UserCurrentLoad.as_view(), name='UserCurrentLoad'),
    path('recept/<int:id>/', views.ListCurrentRecept.as_view(), name='ListCurrentRecept'),
    path('comments/<int:id>/', views.ListCurrentComments.as_view(), name='ListCurrentComments'),
    path('addrecept/', views.AddRecept.as_view(), name='add_recept'),
    path('addcomment/', views.AddComment.as_view(), name='add_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

