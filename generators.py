simple_logins = ['admin', 'jack', 'cat']


def generate_simple_login(state):
    """
    генератор простых логинов из списка simple_logins. На входе номер текущей итерации, на выходе логин и номер
    следующей итерации

    """
    #если первая итерация, то значение state = 0
    if state is None:
        state = 0
    # если последняя итерация, то следующая будет 0
    if state == len(simple_logins) - 1:
        next_state = None
    else:
        next_state = state + 1

    return simple_logins[state], next_state


with open('10-million-password-list-top-1000000.txt') as f:
    popular_passwords = f.read().split('\n')


def generate_popular_password(state):
    """
    генератор популярных паролей из файла. На входе номер текущей итерации, на выходе пароль и номер
    следующей итерации

    """
    if state is None:
        state = 0

    if state == len(popular_passwords) - 1:
        next_state = None
    else:
        next_state = state + 1

    return popular_passwords[state], next_state


alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)


def generate_by_brute_force(state):
    """
    #генератор паролей из строки alphabet. На входе номер текущей итерации, на выходе пароль и номер
    следующей итерации

    """
    if state is None:
        state = [0, 0]
    #учитывается длина пароля
    i, length = state

    password = ''
    temp = i
    while temp != 0:
        rest = temp % base
        temp = temp // base
        password = alphabet[rest] + password
    #добавляем 0 к началу пароля
    password = alphabet[0] * (length - len(password)) + password
    #если дошли до кона строки alphabet, увеличиваем длину пароля на 1 и начинаем с начала строки
    if password == alphabet[-1] * length:
        length += 1
        i = 0
    else:
        i += 1

    next_state = [i, length]

    return password, next_state
