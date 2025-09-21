from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html', {
        'name': 'Llamado T. Vallar III',
        'student_id': '2019-05982'
    })

# Create your views here.
