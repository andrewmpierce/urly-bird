from django.shortcuts import render
from django.views import generic
from django.core import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
class IndexView(generic.Listview):
    template_name = 'template/click_detail.html'
    context_object_name = 'clicks'
    paginate_by=6

    def get_query_set(self):
        return Click.objects.order_by('-timestamp')


def author_clicks(request):     # can probably just get these with a sort
    pass

#
# def all_clicks(request):
#     clicks = Clicks.object.all()
#     clicks_strings = [str(clicks) for click in clicks]
#     return HttpResponse('<br>'.join(clicks_strings))


clicks = clicks.prefetch_related('user')

paginator = Paginator(clicks, 20)
        page = request.GET.get('page')
    try:
        clicks = paginator.page(page)
    except PageNotAnInteger:
        # If page number is not an integer, gotot first page
        clicks = paginator.page(1)
    except EmptyPage:
        # If page number is out of range, give last page
        clicks = paginator.page(paginator.num_pages)
    return render(request,
                  'urly/clicks.html'),
                  {'clicks': clicks}
