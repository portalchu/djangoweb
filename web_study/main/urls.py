from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    # <자료형:파라미터 이름> 데이터를 views로 보내는 기능
    path('blog/<int:pk>', views.posting, name='posting'),
    path('blog/new_post', views.new_post, name='new_post'),
    path('blog/<int:pk>/remove', views.remove_post, name='remove_post'),
]
# 이미지 출력을 위한 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)