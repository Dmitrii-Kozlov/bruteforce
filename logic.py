def iterate_by_passwords_then_by_logins(login_generator, password_generator, query):
    """
    для каждого пароля осуществляется перебор логинов и проверка на сервере. при получении подтверждения от сервера,
    выводит на консоль логин и пвроль
    :param login_generator: генератор из файла generators.py
    :param password_generator: генератор из файла generators.py
    :param query: запрос к серверу из файла queries.py
    """
    password_state = None
    while True:
        password, password_state = password_generator(password_state)

        login_state = None
        while True:
            login, login_state = login_generator(login_state)
            if query(login, password):
                print('Success', login, password)
            if login_state is None:
                break

        if password_state is None:
            break


def iterate_by_logins_then_by_limited_passwords(login_generator, password_generator, query):
    """
    для каждого логина осуществляется перебор пароля и проверка на сервере. при получении подтверждения от сервера,
    выводит на консоль логин и пвроль. Количество переборов пароля ограничено параметром limit
    :param login_generator: генератор из файла generators.py
    :param password_generator: генератор из файла generators.py
    :param query: запрос к серверу из файла queries.py
    """
    limit = 100000
    login_state = None
    while True:
        login, login_state = login_generator(login_state)
        password, password_state = password_generator(None)
        for i in range(limit):
            if query(login, password):
                print('Success', login, password)
                break
            password, password_state = password_generator(password_state)
            if password_state is None:
                break

        if login_state is None:
            break
