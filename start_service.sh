mkdir -p logs
python manage.py migrate
supervisord -c /project/config/supervisord.conf