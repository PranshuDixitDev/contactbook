from django.urls import path
from . import views
urlpatterns=[
    path('<int:pk>/',views.employees_detail, name='employee_detail'),
]