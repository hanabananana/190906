
# 2번줄: admin임포트 삭제
from django.urls import path
from . import views
# 4번줄: 어떤 것에서든 views를 임포트한다.

app_name = 'blog'
urlpatterns = [
    path('', views.postList, name='postList'), # localhost:8000/blog/

]

