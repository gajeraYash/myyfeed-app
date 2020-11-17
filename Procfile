web: gunicorn CS490.wsgi
web: daphne CS490.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channel_layer -v2