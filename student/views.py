from django.shortcuts import render, redirect
from .forms import StudentForm

def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            request.session['student'] = form.cleaned_data
            return redirect('student_result')
    else:
        form = StudentForm()
    return render(request, 'student/student.html', {'form': form})

def student_result(request):
    data = request.session.get('student')
    return render(request, 'student/student_result.html', {'data': data})