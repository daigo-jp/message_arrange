from django.urls import path
from . import views

app_name = 'arrange_message'

urlpatterns = [
    path('', views.home, name='home'),
    path('gemini/', views.message_input, name='input_gemini'),
]