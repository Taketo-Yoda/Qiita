import requests


# ツールサーバーのAPIエンドポイント
SEARXNG_API_URL = "http://localhost:8080/search"

def search(query: str) -> str:
    """
    SearXNGを使って、指定されたクエリで情報を検索するツール。
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(
            SEARXNG_API_URL,
            params={"q": query, "format": "json"},
            headers=headers
        )
        response.raise_for_status()
        results = response.json().get("results", [])[:3]
        return "\n".join([str(r) for r in results])
    except requests.exceptions.RequestException as e:
        return f"SearXNGへのリクエスト中にエラーが発生しました: {e}"
    except Exception as e:
        return f"SearXNGのレスポンス解析中にエラーが発生しました: {e}"

# Google ADKにツールを登録
leisure_tools = [search]
