# Тестовый файл для проверки SAST в Topscan.
# Уязвимости добавлены намеренно — НЕ использовать в реальном проекте.

import hashlib
import os
import pickle
import sqlite3
import subprocess

# 1. Захардкоженный пароль в коде
DB_PASSWORD = "SuperSecret123!"


# 2. SQL-инъекция: пользовательский ввод склеивается с запросом
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


# 3. Command injection: ввод попадает в shell-команду
def ping_host(host):
    return subprocess.call("ping -c 1 " + host, shell=True)


# 4. Выполнение произвольного кода через eval
def calculate(expression):
    return eval(expression)


# 5. Слабый алгоритм хеширования паролей
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


# 6. Небезопасная десериализация
def load_data(raw_bytes):
    return pickle.loads(raw_bytes)


# 7. Ещё одна command injection через os.system
def delete_file(filename):
    os.system("rm " + filename)
