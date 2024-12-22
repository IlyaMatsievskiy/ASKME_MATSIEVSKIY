# Запуск сайта ASKME_MATSIEVSKIY

В этом документе описывается, как запустить серверное приложение, используя Gunicorn, Nginx и встроенный сервер разработки Django.

---

## 1. Запуск Gunicorn

Gunicorn используется для обработки запросов на сервере.

Для запуска Gunicorn выполните следующую команду:

```bash
gunicorn ASKME_MATSIEVSKIY.wsgi
```

Gunicorn будет по умолчанию слушать запросы на порту `8000`. Если вы хотите указать другой порт, добавьте параметр `--bind`:

```bash
gunicorn --bind 127.0.0.1:8080 ASKME_MATSIEVSKIY.wsgi
```

---

## 2. Запуск Nginx

Nginx используется как веб-сервер для обработки статики и проксирования запросов к Gunicorn.

### Запуск Nginx:

Чтобы запустить Nginx, выполните команду:

```bash
sudo nginx
```

### Проверка статуса Nginx:

Чтобы убедиться, что Nginx запущен, выполните:

```bash
sudo nginx -t
```

### Перезапуск Nginx:

Если вы внесли изменения в конфигурацию Nginx, перезапустите сервер:

```bash
sudo nginx -s reload
```

---

## 3. Запуск встроенного сервера разработки Django

Django предоставляет встроенный сервер разработки, который подходит для тестирования и отладки.

Для запуска выполните команду:

```bash
python manage.py runserver
```

По умолчанию сервер запустится на порту `8000`. Чтобы указать другой порт, добавьте его:

```bash
python manage.py runserver 8080
```

---

## 4. Включение real-time сообщений через Centrifugo

Для включения real-time сообщений через Centrifugo выполните следующую команду (в случае если у вас установлен Docker):

```bash
docker run --rm --ulimit nofile=262144:262144 \
  -v /Users/ilya/PycharmProjects/ASKME_MATSIEVSKIY/centrifugo:/centrifugo \
  -p 8010:8000 \
  centrifugo/centrifugo:v5 \
  centrifugo -c /centrifugo/config.json
```

---

## 5. Обновление кэша популярных тегов и лучших пользователей

Для обновления кэша вы можете воспользоваться следующими командами:

- **Обновление кэша популярных тегов:**

```bash
python manage.py cache_popular_tags
```

Эта команда обновляет кэш популярных тегов. Используйте её, если вы хотите обновить данные раньше автоматического обновления.

- **Обновление кэша лучших пользователей:**

```bash
python manage.py cache_best_users
```

Эта команда обновляет кэш лучших пользователей. Используйте её, если вы хотите обновить данные раньше автоматического обновления.

- **Генерация данных для базы:**

```bash
python manage.py fill_db
```

Эта команда используется для заполнения базы данных тестовыми данными.

---

## 6. Настройка Cron для автоматического обновления кэша

Чтобы автоматически обновлять кэш для популярных тегов и лучших пользователей, настройте Cron следующим образом:

1. Откройте редактор Cron:

   ```bash
   crontab -e
   ```

2. Добавьте следующие строки:

   ```bash
   * * * * * cd /Users/ilya/PycharmProjects/ASKME_MATSIEVSKIY && /Users/ilya/PycharmProjects/ASKME_MATSIEVSKIY/venv/bin/python manage.py cache_popular_tags
   * * * * * cd /Users/ilya/PycharmProjects/ASKME_MATSIEVSKIY && /Users/ilya/PycharmProjects/ASKME_MATSIEVSKIY/venv/bin/python manage.py cache_best_users
   ```

Эти строки запускают команды обновления кэша каждую минуту. Вы можете настроить другой интервал, изменив формат Cron.

---

Теперь вы можете запустить сайт, используя один из вышеуказанных способов. Убедитесь, что необходимые зависимости установлены и настроены правильно!
