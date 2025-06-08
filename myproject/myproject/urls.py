from django.contrib import admin
from django.urls import path, include # include が必要です

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # この一行が `http://127.0.0.1:8000/` へのアクセスを
    # `arrange_message` アプリに繋ぐための重要な設定です。
    path('', include('arrange_message.urls')), 
]