mkdir -p logs
python manage.py migrate
python manage.py loaddata regions.json
python manage.py loaddata attributes.json
python manage.py loaddata categories.json
python manage.py loaddata users.json
python manage.py loaddata profile.json
python manage.py loaddata statics
python manage.py collectstatic --noinput
cp -rf static/* assets/
supervisord -c /project/config/supervisord.conf