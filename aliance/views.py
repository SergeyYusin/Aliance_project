from django.shortcuts import render
from .models import Person, Applications
from django.http import HttpResponseNotFound, HttpResponse


# Create your views here.
def app(request):
    context = {
        'app': Applications.objects.all()
    }
    return render(request, 'app.html', context)


def search_app(request):
    cont = 0
    list_app = []
    district = request.GET['district']
    for app in Applications.objects.all():
        if app.district == district:
            cont += 1
            list_app.append(app)
    context = {
        'cont': cont,
        'list_app': list_app
    }
    return render(request, 'app.html', context)

def main(request):
    context = {
        'persons': Person.objects.all()
    }
    return render(request, 'index.html', context)


def search(request):
    cont = 0
    name = request.GET['name']
    last_name = request.GET['last_name']
    for con in Person.objects.all():
        if con.name == name and con.last_name == last_name:
            cont = con.product

    context = {
        'name': name,
        'last_name': last_name,
        'persons': Person.objects.all(),
        'cont': cont
    }
    return render(request, 'search.html', context)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")



