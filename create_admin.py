#!/usr/bin/env python
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freecourses.settings')
django.setup()

from django.contrib.auth.models import User

# Create admin user
username = 'admin'
email = 'admin@example.com'
password = 'admin123'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Admin user created successfully!")
    print(f"Username: {username}")
    print(f"Password: {password}")
else:
    print("Admin user already exists!")
    print(f"Username: {username}")
    print(f"Password: {password}")