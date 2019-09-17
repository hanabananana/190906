from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
from blog.forms import PostForm
from django.shortcuts import redirect


# Create your views here.
def postList(request):
	# 데이터베이스에 저장된 포스트 데이터를 가지고 온다.
	qs = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# qs에 저장된 테이블 데이터는 student_list저장되고
	# 이는 context 딕셔너리에 실려서 readStudents.html템플릿에 전달된다.
	# 템플릿에서는 context를 통해 전달받은 데이터에 접근할 수 있다.
	context = {'posts': qs}
	return render(request, 'blog/postList.html', context)


def postDetail(request, pk):
	qs = get_object_or_404(Post, pk=pk)
	context = {'post': qs}
	return render(request, 'blog/postDetail.html', context)

def postNew(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			#post.published_date = timezone.now()
			post.save()

			return redirect('blog:postDetail', pk=post.pk)
	else:
		form = PostForm()

	context = {'form': form}
	return render(request, 'blog/postNew.html', context)

def postEdit(request, pk):
	qs = get_object_or_404(Post, pk=pk)

	if request.method == "POST":
		form = PostForm(request.POST, instance=qs)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			#post.published_date = timezone.now()
			post.save()

			return redirect('blog:postDetail', pk=post.pk)

	else:
		form = PostForm(instance=qs)
	
	context = {'form': form}
	return render(request, 'blog/postNew.html', context)


def post_draft_list(request):
	# ONLY unpublished posts from DB
	qs = Post.objects.filter(published_date__isnull=True).order_by('created_date')
	context = {'posts': qs}
	return render(request, 'blog/post_draft_list.html', context)


def post_publish(request, pk):
	qs = get_object_or_404(Post, pk=pk)
	qs.publish()
	return redirect('blog:postDetail', pk=pk)


def post_remove(request, pk):
	qs = get_object_or_404(Post, pk=pk)
	qs.delete()
	return redirect('blog:postList')