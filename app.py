import requests  # HTTPリクエストのライブラリをインポート
import time  # スリープ機能のライブラリをインポート


BASE_URL = "https://hacker-news.firebaseio.com/v0/"  # Hacker NewsのAPIのサイトでの指定URL


def get_top_titles_ids():
    """Hacker NewsからトップタイトルのIDを取得する"""
    response = requests.get(f"{BASE_URL}topstories.json")  # トップタイトルのID取得のリクエスト、#f記法 >>「指定URL+毎回固定の文字列」を生成。

    if response.status_code == 200:  # もし、ステータスコードが200なら、リクエストは成功 >> 次の処理に進む
        return response.json()  # 成功時にIDのリストを返す
    else:
        return []  # それ以外は空リストを返す


def get_title_and_link(title_id):
    """与えられたIDに基づいてタイトルとそのリンクを取得する"""
    response = requests.get(f"{BASE_URL}item/{title_id}.json")  # タイトルIDに基づいたタイトルの詳細をリクエスト

    if response.status_code != 200:
        return None  # リクエスト失敗時にはNoneを返す

    data = response.json()  # レスポンスのJSONを解析
    title = data.get("title")  # データからタイトルを取得
    url = data.get("url")  # データからURLを取得

    if title and url:
        return {"title": title, "link": url}  # タイトルとURLの両方が存在する場合にのみ、その情報を返す
    return None  # タイトルかURLが存在しない場合は、Noneを返す


if __name__ == "__main__":
    for title_id in get_top_titles_ids()[:30]:  # 上位30のタイトルIDについて繰り返す
        time.sleep(1)  # 1秒待機して連続アクセスを避ける
        result = get_title_and_link(title_id)  # タイトルとリンクを取得

        if result:  # タイトルとリンクが存在する場合のみ出力
            print(result)
