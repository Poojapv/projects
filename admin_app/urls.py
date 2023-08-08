from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('employee',views.employee ),
    path('task', views.task),
]