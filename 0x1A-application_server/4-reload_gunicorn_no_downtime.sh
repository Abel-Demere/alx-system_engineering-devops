#!/usr/bin/env bash
# Get the process ID of the Gunicorn master
MASTER_PID=$(pgrep gunicorn)

# Send a HUP signal to the master process to gracefully reload the workers
kill -HUP "$MASTER_PID"
