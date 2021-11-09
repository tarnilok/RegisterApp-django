from django.urls import path
from .views import student_list, student_register, student_detail, student_edit, student_delete

urlpatterns = [
    path('', student_list, name='list'),
    path('register/', student_register, name='add'),
    path('detail/<str:slug>/', student_detail, name='detail'),
    path('edit/<str:slug>/', student_edit, name='edit'),
    path('del/<str:slug>/', student_delete, name='delete'),
]