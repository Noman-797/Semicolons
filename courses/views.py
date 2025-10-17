from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Course, Module, Video, Enrollment

def home(request):
    return render(request, 'home.html')

def courses(request):
    courses = Course.objects.all()
    enrolled_courses = []
    if request.user.is_authenticated:
        enrolled_courses = Enrollment.objects.filter(user=request.user).values_list('course_id', flat=True)
    return render(request, 'courses.html', {'courses': courses, 'enrolled_courses': enrolled_courses})

@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        terms = request.POST.get('terms')
        
        if name and email and terms:
            Enrollment.objects.create(
                user=request.user,
                name=name,
                email=email,
                course=course
            )
            messages.success(request, f'You have successfully pre-registered for {course.title}!')
            return redirect('courses')
    
    return render(request, 'enroll.html', {'course': course})

@login_required
def dashboard(request):
    from .models import Course
    from datetime import date, datetime, timedelta
    import random
    
    # User's enrollments
    enrollments = Enrollment.objects.filter(user=request.user).select_related('course').order_by('-enrolled_at')
    
    # Add progress to enrollments (mock data for now)
    for enrollment in enrollments:
        enrollment.progress = random.randint(10, 90)
    
    # Live sessions (courses with live_class_url)
    live_sessions = []
    for enrollment in enrollments:
        if enrollment.course.live_class_url:
            live_sessions.append({
                'course': enrollment.course,
                'date': date.today() + timedelta(days=random.randint(1, 7)),
                'time': datetime.now().replace(hour=random.randint(14, 20), minute=0)
            })
    
    # Recommended courses (courses user hasn't enrolled in)
    enrolled_course_ids = enrollments.values_list('course_id', flat=True)
    recommended_courses = Course.objects.exclude(id__in=enrolled_course_ids)[:6]
    
    context = {
        'enrollments': enrollments,
        'live_sessions': live_sessions,
        'recommended_courses': recommended_courses,
        'today': date.today(),
    }
    return render(request, 'dashboard.html', context)

@login_required
def enrollments(request):
    if request.user.is_staff:
        # Admin can see all enrollments
        enrollments = Enrollment.objects.all().order_by('-enrolled_at')
    else:
        # Regular users can only see their own enrollments
        enrollments = Enrollment.objects.filter(user=request.user).order_by('-enrolled_at')
    return render(request, 'enrollments.html', {'enrollments': enrollments})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        else:
            user = User.objects.create_user(username=email, email=email, password=password1)
            user.first_name = full_name
            user.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('home')

@login_required
def modules(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    # Check if user is enrolled
    enrollment = Enrollment.objects.filter(user=request.user, course=course).first()
    if not enrollment:
        messages.error(request, 'You are not enrolled in this course')
        return redirect('courses')
    
    return render(request, 'modules.html', {'course': course})

@login_required
def course_modules(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    # Check if user is enrolled
    enrollment = Enrollment.objects.filter(user=request.user, course=course).first()
    if not enrollment:
        messages.error(request, 'You are not enrolled in this course')
        return redirect('courses')
    
    modules = Module.objects.filter(course=course).prefetch_related('videos')
    return render(request, 'course_modules.html', {'course': course, 'modules': modules})

@login_required
def profile(request):
    from .models import UserProfile
    from .forms import UserProfileForm
    
    # Ensure profile exists
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'profile.html', {'form': form})