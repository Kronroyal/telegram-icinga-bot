#!/bin/bash
set -e
exec python3 bot.py -d &
echo "Running in daemon mode...."
exec python3 bot.py -m test message