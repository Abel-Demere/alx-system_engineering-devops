#!/usr/bin/env bash
# Fetch the process ID of the Gunicorn master
MASTER_PID=$(pgrep gunicorn)

# Trigger a graceful worker reload by sending a HUP signal to the master process
kill -HUP "$MASTER_PID"
