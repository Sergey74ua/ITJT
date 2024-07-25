from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Course
from .forms import CourseForm

def course(request):
    data = {
        'title': 'ITJT: Course',
        'courseList': Course.objects.all()
    }
    return render(request, 'course.html', data)

def courseCreate(request):
    error = ''
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course')
        else:
            error = 'Форма заполнена неверно'

    form = CourseForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'course/courseCreate.html', data)


class CourseDetail(DetailView):
    model = Course
    template_name = 'course/courseDetail.html'
    context_object_name = 'course'

class CourseUpdate(UpdateView):
    model = Course
    template_name = 'course/courseUpdate.html'
    form_class = CourseForm

class CourseDelete(DeleteView):
    model = Course
    success_url = '/course/'
    template_name = 'course/courseDelete.html'
