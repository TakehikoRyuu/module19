from django.shortcuts import render

def hello_temp(request):
    return render(request, 'start.html')  # Рендерим func_template.html
# Create your views here.
