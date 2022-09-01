from django.urls import path
from api import views

urlpatterns = [
    path('stucreate/', views.hello_world),
    path('stucreate/<int:pk>', views.hello_world),
]