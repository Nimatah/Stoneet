NAME="project"
DJANGODIR=$PWD
BIND=0.0.0.0
PORT=8000
USER=root
GROUP=$USER
WORKERS_COUNT=5
DJANGO_WSGI_MODULE=project.wsgi

if [ "$DJANGO_DEBUG" == true]
then
  exec python manage.py runserver ${BIND}:${PORT}
else
 exec gunicorn ${DJANGO_WSGI_MODULE}:application \
   --bind ${BIND}:${PORT} \
   --name ${NAME} \
   --workers ${WORKERS_COUNT} \
   --user ${USER}
   --group ${GROUP} \
   --log-level debug
fi
