# accounts/views.py

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

    # ▼▼▼ このメソッドを追加 ▼▼▼
    def form_invalid(self, form):
        """フォームのバリデーションが失敗したときに呼ばれるメソッド"""
        
        # ターミナルにエラー内容を出力する
        print("--- フォームのバリデーションエラー ---")
        print(form.errors.as_json(indent=2))
        print("------------------------------------")
        
        # 本来の処理（エラー付きでページを再表示）も実行
        return super().form_invalid(form)