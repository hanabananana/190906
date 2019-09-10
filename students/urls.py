
# 2번줄: admin임포트 삭제
from django.urls import path
from . import views
# 4번줄: 어떤 것에서든 views를 임포트한다.

app_name = 'students'
urlpatterns = [
    path('reg/', views.regStudent, name='reg'),
    path('regCon/', views.regConStudent, name='regCon'),
    path('all/', views.readStudentAll, name='stuAll'),
    path('<str:name>/det/', views.detStudent, name='stuDet'),
    path('<str:name>/mod/', views.readStudentOne, name='stuMod'),
    path('modCon/', views.modConStudent , name='modCon'),
    path('<str:name>/del/', views.delStudent, name='stuDel'),

]

'''
	/students/reg에 들어오면
	views의 regStudent함수가 실행된다.
	이 urlpattern의 이름은 'reg'로 지정한다.
'''
