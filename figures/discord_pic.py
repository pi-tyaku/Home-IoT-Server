import requests

def send_to_discord(webhook_url, image_path, message=None):
    data = {}
    if message:
        data["content"] = message

    with open(image_path, "rb") as f:
        r = requests.post(
            webhook_url,
            data=data,
            files={"file": (image_path, f)}
        )

    if r.status_code not in (200, 204):
        raise RuntimeError(f"Discord送信失敗: {r.status_code}")

