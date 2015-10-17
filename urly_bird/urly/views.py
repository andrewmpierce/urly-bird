from django.http import HttpResponse
from django.views import generic
from django.core import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, render_to_response
from .models import Click, Stats
from datetime import datetime


class IndexView(generic.ListView):
    template_name = 'template/click_detail.html'
    context_object_name = 'clicks'
    paginate_by=6

    def get_query_set(self):
        return Click.objects.order_by('-timestamp')


def new_url(request):
     return HttpResponse("Thank God something shows up!!!!!")


#
# def author_clicks(request):     # can probably just get these with a sort
#     pass
#

def click_detail():
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
                      'urly/click_detail.html'),
                      {'clicks': clicks}


def short(request, click_short):
    click = Click.objects.get(short=click_short)
    click.accessed += 1
    if request.user.is_authenticated():
        click.record(datetime.now(), request.user)
        click.save()
    else:
        click.record(datetime.now(), "Anonymous")
        click.save()
    return redirect(click.orig)


def stats_detail(request, click_short):
    click = Click.objects.get(short=click_short)
    stats = []
    for stat in click.stats_set.all():
        stats.append({'reader':stat.reader,
                        'timestamp': stat.timestamp})

    return render(request, 'urly/stats_detail.html',
        {'click': click,
        'stats':stats})
