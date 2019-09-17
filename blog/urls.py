
# 2번줄: admin임포트 삭제
from django.urls import path
from . import views
# 4번줄: 어떤 것에서든 views를 임포트한다.

app_name = 'blog'
urlpatterns = [
    path('postList/', views.postList, name='postList'), 
    path('<int:pk>/detail/', views.postDetail, name='postDetail'),
    path('postNew/', views.postNew, name='postNew'),
    path('<int:pk>/postEdit', views.postEdit, name='postEdit'),
    path('drafts/',views.post_draft_list,name='post_draft_list'),
    path('<int:pk>/publish', views.post_publish, name='post_publish'),
    path('<int:pk>/remove/', views.post_remove, name='post_remove'),

]

