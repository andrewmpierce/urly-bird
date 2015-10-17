
from django.shortcuts import render, redirect, render_to_response, HttpResponse
from .models import Click, Stats
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import timedelta
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from django.utils import timezone
from PIL import Image
from matplotlib.figure import Figure


# Create your views here.

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
                  'urly/click_detail.html',
                 {'clicks': clicks})


def short(request, click_short):
    click = Click.objects.get(short=click_short)
    click.accessed += 1
    if request.user.is_authenticated():
        #Need to update this view to create a new stats object
        click.record(datetime.now(), request.user)
        click.save()
    else:
        click.record(datetime.now(), "Anonymous")
        click.save()
    return redirect(click.orig)

def graph():
    x = [1,2,3,4,5]
    y = [1,2,3,4,5]
    plot(x,y)
    pylab.show()



def stats_detail(request, click_short):
    click = Click.objects.get(short=click_short)
    stats_list = []
    for stat in click.stats_set.all():
        stats_list.append({'reader':stat.reader,
                        'timestamp': stat.timestamp})
    return render(request, 'urly/stats_detail.html',
        {'click': click,
        #'stats': stats,
        'stats_list':stats_list})

def stats_chart(request, click_pk):
    day_counts = {}
    stats = Stats.objects.filter(click=click_pk).filter(timestamp__gte=timezone.now() - timedelta(days=30))
    for stat in stats:
        if stat.timestamp.day not in day_counts:
            day_counts[stat.timestamp.day] = 1
        else:
            day_counts[stat.timestamp.day] +=1
    day_counts = sorted(day_counts.items(), key=lambda x: x[0])
    x_vals = []
    y_vals = []
    for x in day_counts:
        x_vals.append(x[0])
        y_vals.append(x[1])
    fig = plt.figure()
    #fig.patch.set_alpha(0)
    plt.plot(x_vals,y_vals)
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
