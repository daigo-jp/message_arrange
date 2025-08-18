from django.contrib import admin
from django.urls import path, include # include が必要です

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('home/', include('arrange_message.urls')), 
    path('', include('accounts.urls')),  # accountsアプリのURLを追加
]