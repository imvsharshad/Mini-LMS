#!/user/bin/env.bash

set -o errexit

pip install -r requirements.txt

pip manage.py collectstatic --noinput

pip manage.py migrate