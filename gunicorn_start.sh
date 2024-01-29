#!/bin/sh
NAME="esmax"
DJANGODIR="/var/www/html/esmaxws"
NUM_WORKERS=3
echo "Starting Esmax Api CL Django Application"
cd $DJANGODIR
exec gunicorn -w $NUM_WORKERS $NAME.wsgi:application --bind 127.0.0.1:8001