from django.shortcuts import redirect, render
from cv.repositories.eloquent.collaborator_repository import CollaboratorRepository
from django.contrib import messages


def form_work_with_us(request):
    if request.method == 'POST':
        repository = CollaboratorRepository()
        result = repository.create_collaborator(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            file=request.FILES.get('file')
        )

        if result.get('success') is True:
            messages.success(request, "Candidatura realizada com sucesso!")
            return redirect('work_with_us')
        messages.error(request, result.get('message', 'Erro desconhecido'))
        return render(request, 'work_with_us/create.html', {'error': result.get('message')})

    return render(request, 'work_with_us/create.html')
