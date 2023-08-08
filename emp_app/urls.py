from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home),
    path('signup', views.signup),
    path('dashboard', views.dashboard),
    path('mark-completed/<int:id>/', views.mark_as_completed),
]