# Программа для подбора паролей

Как пользоваться:

в файле queries.py в функции request_local_server установить адрес страницы с 
идентификацией (http://...), и выбрать метод передачи логина\пароля (json...)


def request_local_server(login, password):
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': login, 'password': password})
    return response.status_code == 200
   
   
    
в файле generators.py в переменную simple_logins передать список логинов, для генерации
 популярных паролей используется файл "10-million-password-list-top-1000000.txt" данные
  из которого передаются в переменную popular_passwords. Для генерации неизвестного 
  пароля используется строка '0123456789abcdefghijklmnopqrstuvwxyz' в переменной
  alphabet
  
  
в файле main.py можно выбрать общую логику перебора:
- чтобы для каждого логина перебирать список паролей необходимо указать:

logic.iterate_by_logins_then_by_limited_passwords(
...
)
    
- чтобы для каждого пароля перебирать список логинов необходимо указать:
logic.iterate_by_passwords_then_by_logins(
...
)

и передать в виде аргументов генераторы логина, пароля и запросов:
    generators.generate_simple_login,
    generators.generate_popular_password,
    queries.request_local_server