from django.urls import path
from .views.homepage import homepage
from .views.work_with_us import work_with_us
from .views.form_work_with_us import form_work_with_us

urlpatterns = [
    path('', homepage, name='homepage'),
    path('trabalhe-conosco/', work_with_us, name='work_with_us'),
    path('store/', form_work_with_us, name='form_work_with_us')
]
