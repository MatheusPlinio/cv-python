from django.urls import path
from .views.homepage import homepage
from .views.work_with_us import work_with_us

urlpatterns = [
    path('', homepage, name='homepage'),
    path('trabalhe-conosco/', work_with_us, name='work_with_us')
]
