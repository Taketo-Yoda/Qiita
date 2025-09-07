from google.adk.agents import Agent
from leisure_recommend.tools import leisure_tools

# エージェントの初期化
root_agent = Agent(
        name="leisure_recommender",
        description="レジャー提案エージェント",
        model="gemini-2.0-flash",
        instruction="""
            あなたはレジャー提案の専門AIです。
            ユーザーが行き先や日程を尋ねたら、必ずSearXNGツールで行き先の住所を自律的に検索し、
            その住所を使って次は天気予報をSearXNGツールで検索してください。
            天気が雨の場合は、屋内施設や晴れの日程を提案してください。
            ユーザーが明示的に指示しなくても、必要な情報は自分で検索・取得して判断してください。
        """,
        tools=leisure_tools
    )
