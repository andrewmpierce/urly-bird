from django.shortcuts import render
from django.core import Paginator, EmptyPage, PageNotAnInteger



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
                      'urly/click_detail.html'),
                      {'clicks': clicks}
