from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    name = 'Моргунов Кирилл Витальевич'
    height = '169'
    weight = '62'
    age = '16'
    return render(request, 'about.html',
                  {'name': name, 'height': height, 'weight': weight, 'age': age})


def contacts(request):
    info_dict = {'phone': '+79393057478',
                 'telegram': '@kirich12321',
                 }
    return render(request, 'contacts.html', context={'info': info_dict})


def form(request):
    return render(request, 'form.html')