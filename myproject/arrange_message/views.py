from django.shortcuts import render
import google.generativeai as genai
import os
from django.http import HttpResponseServerError
from .models import MessageData
from datetime import datetime
from zoneinfo import ZoneInfo
from django.views import View
class HomeView(View):
    def get(self, request):
        datetime_now=datetime.now(ZoneInfo('Asia/Tokyo')).strftime('%Y年%m月%d日%H時%M分%S秒')
        return render(request, 'home.html'
                      ,{'datetime_now':datetime_now})
    
class ArrangeMessageView(View):
    def message_input_view(request):
        if request.method == 'POST':
            original_message = request.POST.get('user_message')

            if not original_message:
                # 簡単なバリデーション
                return render(request, 'arrange_message/input_form.html', {'error': 'メッセージを入力してください。'})

            try:
                # Gemini APIキーの設定
                api_key = os.getenv("GOOGLE_API_KEY")
                if not api_key:
                    # 実際にはログに出力するなど、より丁寧なエラー処理を推奨
                    return HttpResponseServerError("APIキーが設定されていません。")
                genai.configure(api_key=api_key)

                # 使用するモデル (例: gemini-1.5-flash-latest)
                model = genai.GenerativeModel('gemini-1.5-flash-latest')

                # プロンプトの作成
                prompt = f"以下の文章をビジネスシーンで使える丁寧な敬語に変換してください。\n\n原文:\n{original_message}\n\n変換後:"

                # Gemini APIでメッセージを変換
                response = model.generate_content(prompt)
                arranged_message_text = response.text

            except Exception as e:
                # API呼び出しや処理中にエラーが発生した場合
                # 実際にはログに出力するなど、より丁寧なエラー処理を推奨
                print(f"Gemini APIエラー: {e}")
                return render(request, 'arrange_message/input_form.html', {
                    'error': f'メッセージの変換中にエラーが発生しました: {e}',
                    'original_message': original_message # 入力値をフォームに復元
                })

            try:
                # データベースに保存
                MessageData.objects.create(
                    message=original_message,
                    arrange_message=arranged_message_text
                )
                # 保存後、同じページにリダイレクトするか、成功ページにリダイレクト
                # ここでは例として、成功メッセージをコンテキストに含めて再度フォームを表示
                return render(request, 'arrange_message/input_form.html', {
                    'success_message': 'メッセージを変換し、保存しました。',
                    'original_message_saved': original_message,
                    'arranged_message_saved': arranged_message_text
                })

            except Exception as e:
                # データベース保存エラー
                print(f"データベース保存エラー: {e}")
                return render(request, 'arrange_message/input_form.html', {
                    'error': f'データベースへの保存中にエラーが発生しました: {e}',
                    'original_message': original_message
                })

        # GETリクエストの場合、または処理完了後
        return render(request, 'arrange_message/input_form.html')


home=HomeView.as_view()
message_input=ArrangeMessageView.as_view()