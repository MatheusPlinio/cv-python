from django.shortcuts import render


def homepage(request):
    context = {}
    return render(request, 'cv/index.html', context)
