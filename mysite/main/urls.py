from django.urls import path
from . import views
#from .views import *

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('notice/', views.notice_list, name='notice_list'),
    path('notice/<int:pk>', views.notice_view, name='notice_view'),
    path('notice/add/', views.notice_add, name='notice_add'),
    path('notice/remove/<int:pk>', views.notice_remove, name='notice_remove'),
]
