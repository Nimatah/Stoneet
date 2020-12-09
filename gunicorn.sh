NAME="project"
DJANGODIR=$PWD
BIND=0.0.0.0
PORT=8000
USER=root
GROUP=$USER
WORKERS_COUNT=1
DJANGO_WSGI_MODULE=project.wsgi

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name ${NAME} \
  --workers ${WORKERS_COUNT} \
  --user ${USER}
  --group ${GROUP} \
  --log-level debug \
  --bind ${BIND}:${PORT}
