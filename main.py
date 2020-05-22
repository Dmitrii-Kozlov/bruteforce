"""
файл запуска программы. выбирается логика работы из файла logic.py ей передаются генераторы паролей и логинов из
файла generators.py и метод отправки на сервер из файла queries.py
"""

import logic
import queries
import generators

logic.iterate_by_logins_then_by_limited_passwords(
    generators.generate_simple_login,
    generators.generate_popular_password,
    queries.request_local_server
)
