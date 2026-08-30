# Python lessons

Учебный проект с автотестами на Python.

## Lesson 10 — Allure

В рамках задания были доработаны UI-автотесты из урока 7 с использованием:

* Python
* Pytest
* Selenium
* Page Object
* Allure

### Структура

```text
lesson_10/
├── calculator_page.py
├── test_calculator.py
├── login_page.py
├── inventory_page.py
├── cart_page.py
├── checkout_page.py
└── test_shop.py
```

## Запуск тестов

Для запуска всех тестов из `lesson_10` выполните:

```bash
pytest lesson_10 -v
```

## Формирование результатов Allure

Для формирования результатов тестирования выполните:

```bash
pytest lesson_10 --alluredir=allure-results
```

После выполнения тестов появится папка `allure-results`.

## Просмотр Allure Report

Для просмотра отчёта выполните:

```bash
allure serve allure-results
```

После запуска команда автоматически откроет Allure Report в браузере.

Папки `allure-results` и `allure-report` являются результатами работы Allure и могут не загружаться в Git-репозиторий.

Их можно добавить в `.gitignore`:

```text
allure-results/
allure-report/
```
