from django.shortcuts import render
from .forms import RegistrationForm
from django.core.paginator import Paginator
from .models import *


def cart_temp(request):
    return render(request, 'cart.html')


def games_temp(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'games.html', context)


def platform_temp(request):
    return render(request, 'platform.html')


def menu_temp(request):
    return render(request, 'menu.html')


def sign_up(request):
    info = {}
    username_test = None
    buyers = Buyer.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Извлекаем данные из формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            for user in buyers:
                if user.name == username:
                    username_test = user.name
            if username_test != None:
                info['error'] = "Пользователь с таким логином уже существует."
            elif password != repeat_password:
                info['error'] = "Пароли не совпадают."
            else:
                info['message'] = f"Приветствуем, {username}!"
                Buyer.objects.create(name=username, age=age)
                form = RegistrationForm()
    else:
        info['form'] = RegistrationForm()
        return render(request, 'registration_page.html', info)

    info['form'] = form
    return render(request, 'registration_page.html', info)


def news(request):
    posts = News.objects.all().order_by('date')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})

# Create your views here.
