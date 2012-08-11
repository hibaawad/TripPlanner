# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse

def home(request):
    t = loader.get_template('wizard/city.html')
    c = Context({})
    return HttpResponse(t.render(c))

def date(request, city):
    t = loader.get_template('wizard/date.html')
    c = Context({'city': city})
    return HttpResponse(t.render(c))

def theme(request, city, days):
    t = loader.get_template('wizard/theme.html')
    c = Context({'city': city, 'days': days})
    return HttpResponse(t.render(c))


def intensity(request, city, days, theme):
    t = loader.get_template('wizard/intensity.html')
    c = Context({'city': city, 'days': days, 'theme':theme})
    return HttpResponse(t.render(c))

def luxury(request, city, days, theme, intensity):
    t = loader.get_template('wizard/luxury.html')
    c = Context({'city': city, 'days': days, 'theme':theme, 'intensity':intensity})
    return HttpResponse(t.render(c))


