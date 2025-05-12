from django.shortcuts import redirect, render


def form_work_with_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        file = request.FILES.get('file')

        if file:

            with open(f'tmp/{file.name}', 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            print(f"Arquivo recebido: {file.name} ({file.size} bytes)")
        return redirect('page-success')
    return render(request, 'cv/work_with_us.html')
