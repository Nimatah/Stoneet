mkdir -p logs
python manage.py migrate
python manage.py loaddata attributes.json
python manage.py loaddata categories.json
python manage.py loaddata users.json
supervisord -c /project/config/supervisord.conf