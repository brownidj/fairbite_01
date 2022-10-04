from django.http import HttpResponse


# Create your views here.
def index(response):
    return HttpResponse('Hello this is a smart_coffee view')


def simple_view(request):
    return HttpResponse('Simple View')
