from django.shortcuts import render, redirect, render_to_response
from .models import Click
from datetime import datetime


# Create your views here.

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
    render_to_response(request, 'urly/stats_detail.html',
        {'click': click})
