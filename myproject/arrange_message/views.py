# arrange_message/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseServerError
from .models import MessageData
import google.generativeai as genai
import os
from datetime import datetime
from zoneinfo import ZoneInfo

class HomeView(View):
    def get(self, request, *args, **kwargs):
        # 元のコードに閉じ括弧が抜けていたのを修正しました
        return render(request ,'arrange_message/home.html') 


class ArrangeMessageView(View):
    # GETリクエスト（フォームページの表示）を処理するメソッド
    def get(self, request, *args, **kwargs):
        history_list = MessageData.objects.all().order_by('-id')
        context = {
            'history': history_list
        }
        return render(request, 'arrange_message/arrange_gemini.html', context)

    # POSTリクエスト（フォームの送信）を処理するメソッド
    def post(self, request, *args, **kwargs):
        original_message = request.POST.get('user_message')
        history_list = MessageData.objects.all().order_by('-id')
        context = {'history': history_list}

        if not original_message:
            context['error'] = 'メッセージを入力してください。'
            return render(request, 'arrange_message/arrange_gemini.html', context)

        try:
            # Gemini APIキーの設定
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                return HttpResponseServerError("APIキーが設定されていません。")
            genai.configure(api_key=api_key)

            # モデルの選択とプロンプトの作成
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            prompt = f"以下の文章をビジネスシーンで使える丁寧な敬語に変換してください。\n\n原文:\n{original_message}\n\n変換後:"
            
            # Gemini APIでメッセージを変換
            response = model.generate_content(prompt)
            arranged_message_text = response.text

        except Exception as e:
            print(f"Gemini APIエラー: {e}")
            context['error'] = f'メッセージの変換中にエラーが発生しました: {e}'
            context['original_message'] = original_message
            return render(request, 'arrange_message/arrange_gemini.html', context)

        try:
            # データベースに保存
            new_data = MessageData.objects.create(
                message=original_message,
                arrange_message=arranged_message_text
            )
            # 完了画面にリダイレクト。pk に作成したデータのIDを渡す
            return redirect('arrange_message:success', pk=new_data.pk)

        except Exception as e:
            print(f"データベース保存エラー: {e}")
            context['error'] = f'データベースへの保存中にエラーが発生しました: {e}'
            context['original_message'] = original_message
            return render(request, 'arrange_message/arrange_gemini.html', context)

class SuccessView(View):
    # GETリクエスト（成功ページの表示）を処理するメソッド
    def get(self, request, pk, *args, **kwargs):
        saved_data = get_object_or_404(MessageData, pk=pk)
        context = {
            'saved_data': saved_data
        }
        return render(request, 'arrange_message/success.html', context)
    
class MessageListView(View):
    def get(self, request, *args, **kwargs):
        # データベースから全履歴
        history_list = MessageData.objects.all().order_by('-id')
        # コンテキストを渡してテンプレートをレンダリング
        return render(request, 'arrange_message/message_list.html',{'history': history_list} )
    

# .as_view() を使って、クラスをDjangoが使えるビュー関数に変換
home = HomeView.as_view()
message_input = ArrangeMessageView.as_view()
success = SuccessView.as_view()
message_list = MessageListView.as_view()
