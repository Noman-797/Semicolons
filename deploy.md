# Deployment Guide

## Heroku Deployment

1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Set environment variables:
   ```
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set CLOUDINARY_CLOUD_NAME=your-cloud-name
   heroku config:set CLOUDINARY_API_KEY=your-api-key
   heroku config:set CLOUDINARY_API_SECRET=your-api-secret
   ```
5. Deploy: `git push heroku main`
6. Run migrations: `heroku run python manage.py migrate`
7. Create superuser: `heroku run python manage.py createsuperuser`

## Railway Deployment

1. Connect GitHub repo to Railway
2. Set environment variables in Railway dashboard
3. Deploy automatically on push

## Render Deployment

1. Connect GitHub repo to Render
2. Set environment variables in Render dashboard
3. Use build command: `pip install -r requirements.txt`
4. Use start command: `gunicorn freecourses.wsgi:application`