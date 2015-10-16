from django.shortcuts import render, redirect
from .models import Click


# Create your views here.
def short(request, click_short):
    click = Click.objects.get(short=click_short)
    return redirect(click.orig)
