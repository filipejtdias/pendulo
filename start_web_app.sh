#bin/bash

python3 ~/pendulo/app.py 2>&1 | tee ~/pendulo/logs/app.log

python3 ~/pendulo/logs.py
