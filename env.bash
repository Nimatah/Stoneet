if [ "$DJANGO_ENV" == "prod" ]; then
  export DJANGO_DEBUG=false
  export DJANGO_STAGING=false
fi
