#!/usr/bin/env bash
set -o errexit

apt-get update
apt-get install -y libpq-dev
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='aanoman').exists() or User.objects.create_superuser('aanoman', 'aanoman@example.com', 'AANoman@2025')" | python manage.py shell