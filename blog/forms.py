from django import forms

from blog.models import Post

class PostForm(forms.ModelForm): # 장고에게 PostForm클래스는 ModelForm임을 알려준다.
	class Meta:
		model = Post # 폼을 만들기위해 어떤 model을 쓸건지 장고에게 알려주는 구문
		fields = ('title', 'text')

