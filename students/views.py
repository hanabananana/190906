from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from students.models import Student

# Create your views here.
def regStudent(request):
	return render(request, 'students/registerStudent.html')


def regConStudent(request):
	name = request.POST['name']
	major = request.POST['major']
	age = request.POST['age']
	grade = request.POST['grade']
	gender = request.POST['gender']
	

	# 데이터베이스에 request로부터 전달받은 데이터를 테이블에 저장하는 쿼리
	qs = Student(s_name = name, s_major = major, s_age=age, s_grade=grade, s_gender = gender)
	qs.save()

	# 마지막으로 웹페이지사용자에게 "학생전체보기 페이지" url인 students/all 에 연결시켜준다.
	return HttpResponseRedirect(reverse('students:stuAll'))


def readStudentAll(request):
	# 데이터베이스에 저장된 모든데이터를 가져온다.
	qs = Student.objects.all()
	# qs에 저장된 테이블 데이터는 student_list저장되고
	# 이는 context 딕셔너리에 실려서 readStudents.html템플릿에 전달된다.
	# 템플릿에서는 context를 통해 전달받은 데이터에 접근할 수 있다.
	context = {'student_list': qs}
	return render(request, 'students/readStudents.html', context)


def detStudent(request, name):
	qs = Student.objects.get(s_name = name)
	context = {'student_info': qs}
	return render(request, 'students/detailStudent.html', context)


def readStudentOne(request, name):
	qs = Student.objects.get(s_name = name)
	context = {'student_info': qs}
	return render(request, 'students/modifyStudent.html', context)

def modConStudent(request):
	# modifyStudent.html로부터 수정된 학생데이터를 가져온다.
	name = request.POST['name']
	major = request.POST['major']
	age = request.POST['age']
	grade = request.POST['grade']
	gender = request.POST['gender']

	# 데이터베이스에서 특정 학생의 데이터를 가져온다.
	s_qs = Student.objects.get(s_name=name)

	# 데이터베이스의 값을 수정된값으로 바꾼다.
	s_qs.s_name = name
	s_qs.s_major = major
	s_qs.s_age = age
	s_qs.s_grade = grade
	s_qs.s_gender = gender

	s_qs.save()

	# 사용자의 페이지를 학생전체보기페이지로 리디랙트한다.
	return HttpResponseRedirect(reverse('students:stuAll'))

def delStudent(request, name):
	qs = Student.objects.get(s_name=name)
	qs.delete()

	return HttpResponseRedirect(reverse('students:stuAll'))
