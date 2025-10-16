#!/usr/bin/env python
"""
Setup script for Free Course Enrollment Website
This script will:
1. Create and run database migrations
2. Create sample course data

Usage: python setup.py
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freecourses.settings')
django.setup()

from courses.models import Course

def create_sample_courses():
    """Create sample courses for testing"""
    # Delete all existing courses first
    Course.objects.all().delete()
    
    from datetime import date, timedelta
    
    course_data = {
        'title': 'Full Stack Development with Django',
        'description': 'Master full-stack web development using Django framework, HTML, CSS, JavaScript and build complete web applications from scratch.',
        'start_date': date.today() + timedelta(days=30)  # Course starts 30 days from now
    }
    
    course, created = Course.objects.get_or_create(
        title=course_data['title'],
        defaults={
            'description': course_data['description'],
            'start_date': course_data['start_date']
        }
    )
    if created:
        print(f"Created course: {course.title}")
    else:
        print(f"Course already exists: {course.title}")

if __name__ == '__main__':
    print("Setting up Free Course Enrollment Website...")
    
    # Run migrations first
    print("Running migrations...")
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'makemigrations'])
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Create sample courses
    print("Creating sample courses...")
    create_sample_courses()
    print("Setup completed successfully!")
    print("Run 'python manage.py runserver' to start the development server.")
    print("Visit http://127.0.0.1:8000/ to view the website.")