from django.urls import path
from .views import create_paste, paste_list, paste_edit
urlpatterns = [
    path('create/', create_paste, name='create_paste'),
    path('list/', paste_list, name='paste_list'),
    path('edit/<int:pk>', paste_edit, name="paste_edit")
    
]