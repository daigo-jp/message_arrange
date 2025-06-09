from datetime import datetime
from zoneinfo import ZoneInfo

def common_variables(request):
    """
    全てのテンプレートで共通して使用する変数を返す
    """
    return {
        'current_time': datetime.now(ZoneInfo('Asia/Tokyo')).strftime('%Y年%m月%d日 %H時%M分%S秒')
    }