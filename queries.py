import requests


def request_local_server(login, password):
    """
    проверка логина и пароля при запросе к указанному серверу. формат JSON
    """
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': login, 'password': password})
    # if response.status_code == 200:
    #     return True
    # else:
    #     return False
    return response.status_code == 200


def request_protected_local_server(login, password):
    """
    проверка логина и пароля при запросе к указанному серверу. формат JSON
    """
    response = requests.post('http://127.0.0.1:4000/auth',
                             json={'login': login, 'password': password})
    return response.status_code == 200
