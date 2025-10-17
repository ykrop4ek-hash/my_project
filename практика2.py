def logger(func):
    def wrapper(*args, **kwargs):
        if kwargs:
            print(f"Вызов функции {func.__name__} с аргументами {args} {kwargs}")
        else:
            print(f"Вызов функции {func.__name__} с аргументами {args}")
        try:
            result = func(*args, **kwargs)
            print(f"Функция {func.__name__} вернула {result}")
            return result
        except Exception as e:
            print(f"Функция {func.__name__} вызвала ошибку: {e}")
            return None
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def divide(x, y):
    if y == 0:
        raise ValueError("Деление на ноль невозможно")
    return x / y


@logger
def greet(name):
    message = f"Hi, {name}!"
    print(message)
    return message

add(54, 12)
divide(21, 6)
divide(36, 0)
greet("Peter")

def require_role(allowed_roles):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get("role") in allowed_roles:
                return func(user, *args, **kwargs)
            else:
                print(f"Доступ запрещён пользователю {user['name']}")
        return wrapper
    return decorator

@require_role(["admin"])
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")


@require_role(["admin", "manager"])
def view_reports(user):
    print(f"Пользователь {user['name']} просматривает отчёты")


@require_role(["user", "manager", "admin"])
def access_dashboard(user):
    print(f"Пользователь {user['name']} зашёл на панель управления")

user_admin = {"name": "kail", "role": "admin"}
user_manager = {"name": "sub", "role": "manager"}
user_user = {"name": "kwil", "role": "user"}
user_guest = {"name": "ykrop", "role": "guest"}

delete_database(user_admin)
delete_database(user_manager)
view_reports(user_manager)
view_reports(user_guest)
access_dashboard(user_user)
access_dashboard(user_guest)

