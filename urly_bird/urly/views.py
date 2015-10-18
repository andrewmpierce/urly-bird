from django.http import HttpResponse
from django.views import generic
from hashids import Hashids
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, render_to_response
from .models import Click, Stats
from datetime import datetime


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



def new_short_url(request):
    hashids = Hashids()
    user_click = request.user
    hashids = Hashids(min_length=6, salt="thisissalt")
    if request.method == 'POST':
        user_click = Click(author=request.author,
                          title=fake.text(max_nb_chars=15),
                          timestamp=datetime.now(),
                          orig = fake.url(),
                          short = hashids.encode(x))
        user_click.save()
        return render(request, 'urly/homepage.html',{'submitted':True, 'click':user.click})
    return render(request, 'urly/homepage.html')


def click_detail(request):
    clicks = Click.objects.order_by('-timestamp').all()

    paginator = Paginator(clicks, 20)
    page = request.GET.get('page')
    try:
        clicks = paginator.page(page)
    except PageNotAnInteger:
        # If page number is not an integer, goto first page
        clicks = paginator.page(1)
    except EmptyPage:
        # If page number is out of range, give last page
        clicks = paginator.page(paginator.num_pages)
    return render(request, 'urly/click_detail.html', {'clicks': clicks})
