from django.shortcuts import render

# Create your views here.
def postList(request):
	return render(request, 'blog/postList.html', {})