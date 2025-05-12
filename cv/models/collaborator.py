from django.db import models


class Collaborator(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome Completo")
    email = models.EmailField(verbose_name="E-mail")
    phone = models.CharField(max_length=20, verbose_name="Telefone")
    curriculum = models.FileField(upload_to='curriculums/', verbose_name="Currículo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    class Meta:
        verbose_name = "Collaborator"
        verbose_name_plural = "Collaborators"
        ordering = ['name']

    def __str__(self):
        return self.name