#!/usr/bin/env python3
"""
send_discord.py
標準入力またはコマンドライン引数で受け取った文を
Discord Webhook に投稿する最小スクリプト
"""
import os, sys, requests
from dotenv import load_dotenv
load_dotenv()
WEBHOOK_URL = str(os.getenv("WEBHOOK_URL"))  # 必須
ALERT_URL= str(os.getenv("ALERT_URL"))
TEMP_URL= str(os.getenv("TEMP_URL"))
COND_URL= str(os.getenv("COND_URL"))
LUX_URL= str(os.getenv("LUX_URL"))

def send(content: str) -> None:
    """Discord にメッセージを投稿"""
    resp = requests.post(
        WEBHOOK_URL,
        json={"content": content},
        timeout=10,
    )
    # 2xx 以外なら例外を投げて終了
    resp.raise_for_status()

def alert(content: str) -> None:
    """Discord にメッセージを投稿"""
    resp = requests.post(
        ALERT_URL,
        json={"content": content},
        timeout=10,
    )
    # 2xx 以外なら例外を投げて終了
    resp.raise_for_status()

def temp(content: str) -> None:
    """Discord にメッセージを投稿"""
    resp = requests.post(
        TEMP_URL,
        json={"content": content},
        timeout=10,
    )
    # 2xx 以外なら例外を投げて終了
    resp.raise_for_status()

def air(content: str) -> None:
    """Discord にメッセージを投稿"""
    resp = requests.post(
        COND_URL,
        json={"content": content},
        timeout=10,
    )
    # 2xx 以外なら例外を投げて終了
    resp.raise_for_status()
def lux(content: str) -> None:
    resp = requests.post(
        LUX_URL,
        json={"content": content},
        timeout=10,
    )
    # 2xx 以外なら例外を投げて終了
    resp.raise_for_status()

if __name__ == "__main__":
    # 引数優先、なければ stdin
    message = "Hello World!"
    for i in range(10):
        send(message)
        alert(message)
        temp(message)
        air(message)
        lux(message)
