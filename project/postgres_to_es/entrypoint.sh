#!/bin/sh

set -e

if [ -n "$DB_HOST" ]; then
  bash ./wait-for-it.sh "$DB_HOST:$DB_PORT"
fi

if [ -n "$ES_HOST" ]; then
  bash ./wait-for-it.sh "$ES_HOST:$ES_PORT"
fi

python main.py

exec "$@"
