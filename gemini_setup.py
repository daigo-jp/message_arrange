import google.generativeai as genai
import os

# APIキーを設定 (環境変数からの読み込みを推奨)
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("APIキーが環境変数 GOOGLE_API_KEY に設定されていません。")
    genai.configure(api_key=api_key)
except ValueError as e:
    print(f"エラー: {e}")
    exit()
except Exception as e:
    print(f"予期せぬエラーが発生しました: {e}")
    exit()

# Gemini 1.5 Flash モデルを指定
# 'gemini-1.5-flash-latest' は常に最新の安定版を指します
model = genai.GenerativeModel('gemini-1.5-flash-latest')

prompt = "Gemini 1.5 Flashの特徴を3つ教えてください。"

try:
    response = model.generate_content(prompt)
    print(response.text)
except Exception as e:
    print(f"API呼び出し中にエラーが発生しました: {e}")