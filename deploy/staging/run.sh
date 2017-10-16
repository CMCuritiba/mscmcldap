#!/usr/bin/env bash

#source /usr/share/envs/mscmc/bin/activate

cd /usr/share/webapps/mscmcldap

exec /usr/share/envs/mscmc/bin/gunicorn config.wsgi -c deploy/staging/gunicorn.conf.py  --env DJANGO_SETTINGS_MODULE=config.settings.production