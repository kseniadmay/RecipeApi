#!/bin/sh

# Применяем миграции
python manage.py migrate --noinput

# Собираем статику
python manage.py collectstatic --noinput

# Запускаем Gunicorn
exec gunicorn RecipeAPI.wsgi:application --bind 0.0.0.0:$PORT