# Отчёт по CI — День 7

## Workflow
- Файл: `.github/workflows/ci.yml`
- События: push в main, pull_request, workflow_dispatch
- Окружение: ubuntu-latest, Python 3.11 и 3.12 (матрица)
- Команда тестов: `python -m unittest discover -s tests -v`

## Пара 1. Исходный запуск
- URL: https://github.com/s0reen3/pm03-day07/actions/runs/37944009084
- SHA: 20ad5ca
- Результат: 6 методов OK на Python 3.11 и 3.12

## Пара 2. Красный и зелёный run
- Красный run: URL запуска: https://github.com/s0reen3/pm03-day07/actions/runs/37946288611
  - SHA: eaf4183
  - Ветка: ci/boundary
  - Упавший шаг: Run tests
  - Упавшие тесты: test_at_limit, test_high_priority, test_low_priority
  - Сообщение: AssertionError: True is not false
  - Причина: оператор >= вместо > — просрочка срабатывает на границе
- Зелёный run: https://github.com/s0reen3/pm03-day07/actions/runs/37946634025
  - SHA: 8506fb7
  - Результат: 6 методов OK после возврата строгого >
- Коммит с двумя тестами: (SHA коммита "Test invalid SLA inputs")
- Финальный зелёный run в PR: https://github.com/s0reen3/pm03-day07/pull/1
