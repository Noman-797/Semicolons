from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('enrollments/', views.enrollments, name='enrollments'),
    path('modules/<int:course_id>/', views.modules, name='modules'),
    path('course-modules/<int:course_id>/', views.course_modules, name='course_modules'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]