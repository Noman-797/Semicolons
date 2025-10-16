# Free Course Enrollment Website

A Django-based web application for free course enrollment with a modern, responsive design using Tailwind CSS.

## Features

- **User Authentication**: Login/Register system
- **Home Page**: Hero section with call-to-action
- **Courses Page**: Display available courses with enrollment buttons
- **Enrollment Form**: Simple form to enroll in courses (login required)
- **My Enrollments**: Users can view their own enrollments
- **Admin Panel**: Admins can view all enrollments and manage courses

## Tech Stack

- **Backend**: Python Django
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Database**: SQLite (default Django DB)

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup Database and Sample Data**:
   ```bash
   python setup.py
   ```
   
   This will automatically:
   - Create database migrations
   - Apply migrations to create tables
   - Add sample courses

4. **Create Superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

5. **Run Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
freecourses/
├── freecourses/          # Django project settings
├── courses/              # Main Django app
│   ├── templates/        # HTML templates
│   ├── static/          # CSS and JS files
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   └── urls.py          # URL patterns
├── manage.py            # Django management script
├── setup.py             # Database setup script
└── requirements.txt     # Python dependencies
```

## Usage

1. Visit the home page to see the hero section
2. Register a new account or login with existing credentials
3. Click "View Courses" to see available courses
4. Click "Enroll Now" on any course to fill out the enrollment form
5. View your enrollments on the "My Enrollments" page
6. Admins can view all enrollments and use the admin panel to manage courses

## User Types

- **Regular Users**: Can enroll in courses and view their own enrollments
- **Admin Users**: Can view all enrollments and manage courses through admin panel