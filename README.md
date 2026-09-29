# Автотесты для разных языков интерфейса

Решение задания из курса [«Автоматизация тестирования с помощью Selenium и Python»](https://stepik.org/course/575): тест проверяет, что на странице товара интернет-магазина есть кнопка добавления в корзину, а язык интерфейса передаётся из командной строки.

## Файлы

- `conftest.py` — параметр командной строки `--language` и фикстура `browser`, которая запускает Chrome с выбранным языком;
- `test_items.py` — тест `test_product_page_has_add_to_basket_button`.

## Запуск

```bash
pip install selenium pytest
pytest --language=es test_items.py
```

Без параметра `--language` используется английский.

Чтобы глазами проверить язык, раскомментируйте в `test_items.py` строку с `time.sleep(30)` и запустите тест с `--language=fr`: на кнопке должно быть написано «Ajouter au panier».
