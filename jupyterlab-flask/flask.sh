#! /usr/bin/env bash

umask 002
cd /app
python3 -m flask run --host=0.0.0.0

