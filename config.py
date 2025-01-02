import os
from dotenv import load_dotenv

# Загрузка переменных из .env файла
load_dotenv()

# OAuth токен, необходимый для получения IAM токена
OAUTH_TOKEN = os.getenv("OAUTH_TOKEN")

# ID папки Yandex Cloud
FOLDER_ID = os.getenv("FOLDER_ID")

# Путь для сохранения изображений
IMAGES_PATH = os.getenv("IMAGES_PATH", "static/images")

# Базовые URL API Yandex
URL_IAM_TOKEN = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
URL_IMAGE_GENERATION = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"
URL_OPERATIONS = "https://llm.api.cloud.yandex.net:443/operations"
