#!/bin/bash

SCRIPPATH="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $SCRIPPATH; tail -f job.log; source venv/bin/activate; python3 src/app.py $1
