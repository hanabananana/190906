"""jango3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
]


'''

	jango3/urls.py

	프로젝트 생성시 프로젝트폴더인 jango3 안에는 urls.py라는 파일이 있다.
	이 파일에 모든 urlpattern을 모아서 저장한다.

	이 프로젝트에 만든 앱이 많아지고(지금은 students앱 밖에 없지만)
	그 앱에 대한 view가 많아지면 urlpatterns에 들어가는 데이터는 굉장히 많아질 것이다.
	예를들어 students앱에 대한 뷰가 10개라고 할때 
	모든 10개의 뷰에 대한 urlpatterns을 여기에 저장하는 것보다는
	유지보수를 쉽게하기 위해.. 앱 각각의 담당 url로도 이동할 수 있도록하자.

	따라서 students앱폴더 내에 urls.py파일을 새로 하나더 만들도록하고
	여기 이 파일에서 그 urls.py로 이동할 수 있도록 하자.

'''