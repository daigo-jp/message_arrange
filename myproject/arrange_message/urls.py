# arrange_message/urls.py
from django.urls import path
from . import views

app_name = 'arrange_message'

urlpatterns = [
    path('', views.home, name='home'),
    path('gemini/create', views.message_input, name='input_gemini'),
    path('success/<int:pk>/', views.success, name='success'),
    path('message_list/', views.message_list, name='message_list'),

]