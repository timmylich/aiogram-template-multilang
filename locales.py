from aiogram_translation.models import BaseTranslationBuilder

class BaseTranslation(BaseTranslationBuilder):
    test_string: str

class English(BaseTranslation):
    key: str = "en"
    name: str = "English"

    test_string: str = "Test String."

class Russian(English):
    key: str = "ru"
    name: str = "Русский"

    test_string: str = "Тестовая строка."