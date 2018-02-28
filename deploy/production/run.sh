#!/usr/bin/env bash

#source /usr/share/envs/mscmc/bin/activate

cd /usr/share/webapps/mscmcldap

mkdir -p /usr/share/webapps/mscmcldap/var/run
rm -f /usr/share/webapps/mscmcldap/var/run/*

exec /usr/share/envs/mscmc/bin/gunicorn config.wsgi -c deploy/production/gunicorn.conf.py  --env DJANGO_SETTINGS_MODULE=config.settings.production