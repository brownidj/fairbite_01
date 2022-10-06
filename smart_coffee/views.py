from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

pages = {
    'shops': '<h1>Coffee Shops</h1>',
    'volunteers': '<h1>Volunteers</h1>',
    'routes': '<h1>Routes</h1>>'
}


# Create your views here.
def page_view(request, page):
    try:
        result = pages[page]
        return HttpResponse(result)
    except:
        raise Http404('404 Generic Error')


def num_page_view(request, num_page):
    try:
        page_list = list(pages.keys())
        page = page_list[num_page]
        webpage = reverse('page_view', args=[page])
        return HttpResponseRedirect(webpage)
    except:
        raise Http404('404 Generic Error')
