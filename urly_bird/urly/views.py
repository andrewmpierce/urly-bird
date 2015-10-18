from django.shortcuts import render, redirect, render_to_response, HttpResponse
from .models import Click, Stats
from datetime import datetime
from django.utils import timezone
from datetime import timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User




# def click_detail():
#     clicks = clicks.prefetch_related('user')
#
#     paginator = Paginator(clicks, 20)
#     page = request.GET.get('page')
#     try:
#         clicks = paginator.page(page)
#     except PageNotAnInteger:
#         # If page number is not an integer, gotot first page
#         clicks = paginator.page(1)
#     except EmptyPage:
#         # If page number is out of range, give last page
#         clicks = paginator.page(paginator.num_pages)
#     return render(request,
#                   'urly/click_detail.html',
#                  {'clicks': clicks})

def short(request, click_short):
    click = Click.objects.get(short=click_short)
    click.accessed += 1
    if request.user.is_authenticated():
        new_stat = Stats(reader = request.user,
                        click = Click.objects.get(short=click_short),
                        timestamp = datetime.now())
        new_stat.save()
    else:
        new_stat = Stats(reader = "Anonymous",
                        click = Click.objects.get(short=click_short),
                        timestamp = datetime.now())
        new_stat.save()
    return redirect(click.orig)




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
    day_counts = dict((x,0) for x in range(32))
    stats = Stats.objects.filter(click=click_pk).filter(timestamp__gte=timezone.now() - timedelta(days=30))
    for stat in stats:
        # if stat.timestamp.day not in day_counts:
        #     day_counts[stat.timestamp.day] = 1
        day_counts[stat.timestamp.day] +=1
    day_counts = sorted(day_counts.items(), key=lambda x: x[0])
    x_vals = []
    y_vals = []
    for x in day_counts:
        x_vals.append(x[0])
        y_vals.append(x[1])
    fig = plt.figure(figsize=(10,4))
    #fig.patch.set_alpha(0)
    plt.plot(x_vals,y_vals)
    plt.xticks([1,5,10,15,20,25,30])
    plt.title("Popularity of Bookmark for the Previous Month")
    plt.xlabel("Day of the Month")
    plt.ylabel("Number of Clicks")
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


def user_table(request, username):
    user = User.objects.get(username=username)
    clicks = Click.objects.filter(author=user).all()
    return render(request, 'urly/user_table.html',
        {'clicks':clicks,
        'user': user})
