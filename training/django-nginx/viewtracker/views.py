from django.shortcuts import render
from viewtracker.models import PageView


def pageview(request):
    PageView.objects.create()
    return render(request, 'viewtracker/viewcount.html', {'count': PageView.objects.count()})
