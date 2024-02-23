from django.shortcuts import render

# tus vistas existentes...


def about(request):
    return render(request, 'bout.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def course(request):
    return render(request, 'course.html')


def single(request):
    return render(request, 'single.html')


def teacher(request):
    return render(request, 'teacher.html')
