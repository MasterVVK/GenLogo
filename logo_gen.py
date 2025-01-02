from services.yandex_service import YandexArtService

def generate_logo(forma, style, description):
    """
    Генерирует логотип с помощью Yandex-Art API.

    :param forma: Форма логотипа.
    :param style: Стиль логотипа.
    :param description: Описание логотипа.
    :return: Путь к сохраненному изображению или сообщение об ошибке.
    """
    service = YandexArtService()
    prompt = f"Нарисуй логотип в форме {forma}, в стиле {style}, описание: {description}."
    try:
        image_path = service.generate_image(prompt)
        return image_path
    except Exception as e:
        return f"Ошибка генерации изображения: {e}"
