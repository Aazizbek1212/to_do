from django.urls import path
from .views import TaskView, AddTask



urlpatterns = [
    path('', TaskView.as_view(), name='home'),
    path('add/', AddTask.as_view(), name='add')
    
]
