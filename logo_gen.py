import requests
import random
import time
import base64
import os
import config as cfg

def generate_logo(forma, style, description):
    headers = {
        "Authorization": f"Bearer {cfg.iam_token}",
        "Content-Type": "application/json"
    }
    data = {
        "modelUri": f"art://{cfg.catalog_id}/yandex-art/latest",
        "generationOptions": {
            "seed": f"{random.randint(0, 1000000)}",
            "aspectRatio": {
                "widthRatio": "1",
                "heightRatio": "1"
           }
        },
        "messages": [
            {
                "weight": "1",
                "text": f"Нарисуй логотип в форме {forma} под описание: {description}, в стиле: {style}"
            }
        ]
    }
    response = requests.post(cfg.url_1, headers=headers, json=data)
    if response.status_code == 200:
        request_id = response.json()['id']
        time.sleep(20)
        headers.pop("Content-Type")
        response = requests.get(f"{cfg.url_2}/{request_id}", headers=headers)
        if response.status_code == 200:
            image_base64 = response.json()['response']['image']
            image_data = base64.b64decode(image_base64)
            image_path = os.path.join('static', 'image.jpeg')
            with open(image_path, 'wb') as file:
                file.write(image_data)
            return image_path
        else:
            return f"Ошибка ответа: {response.status_code} - {response.text}"
    else:
        return f"Ошибка запроса: {response.status_code} - {response.text}"
