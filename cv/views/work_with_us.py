from django.shortcuts import render

def work_with_us(request):
    context = {}
    return render(request, 'work_with_us/create.html', context)