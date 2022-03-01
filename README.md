Перед запуском необходимо добавить Bucket images в MinIo

И Применить начальные настройки базы данных

Подключаемся к контейнеру django(после запуска через ```sudo docker-compose up -d```)
```sudo docker exec -it django bash```
Переходим в папку с manage.py
```cd /code/```
Собираем файлы статики
```python3 manage.py collectstatic --noinput```
Применяем миграции на бд
```python manage.py migrate```
Создаём аккаунт администратора из env параметров
```python manage.py createsuperuser --noinput```

Также необходимо заменить домены в config/*.conf