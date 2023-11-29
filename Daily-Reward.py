import asyncio
import json

import genshin


async def main():
    json_cookies = open('token.json', 'r')
    cookies = json.load(json_cookies)
    client = genshin.Client(cookies)
    client.lang = "ja-jp"
    client.region = genshin.Region.OVERSEAS
    client.default_game = genshin.Game.GENSHIN
    client.uid = 849157751  # ここgame内のuid(正直なくていい)

    try:
        reward = await client.claim_daily_reward()
        # デイリー報酬を受け取ろうとする
    except genshin.AlreadyClaimed:
        # すでに取られている場合
        print("すでに受け取っています。")
    else:
        # 取れた場合
        print(f"{reward.name}を{reward.amount}個獲得しました")


asyncio.run(main())
