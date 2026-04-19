#!/usr/bin/env sh

set -eu

HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-5000}"
WORKERS="${GUNICORN_WORKERS:-2}"

exec gunicorn --bind "${HOST}:${PORT}" --workers "${WORKERS}" app:app
