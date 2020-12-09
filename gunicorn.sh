NAME="project"
DJANGODIR=$PWD
BIND=0.0.0.0:8000
USER=root
GROUP=$USER
WORKERS_COUNT=3
DJANGO_WSGI_MODULE=project.wsgi

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name ${NAME} \
  --workers ${WORKERS_COUNT} \
  --user=${USER}
  --group=${GROUP} \
  --log-level=debug \
  --bind=${BIND}
