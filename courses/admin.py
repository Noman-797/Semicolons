from django.contrib import admin
from .models import Course, Module, Video, Enrollment, UserProfile
from .forms import CourseForm, UserProfileForm

class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1
    fields = ['title', 'order']

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1
    fields = ['title', 'video_url', 'duration', 'order']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    list_display = ['title', 'start_date', 'created_at']
    list_filter = ['start_date', 'created_at']
    search_fields = ['title', 'description']
    fields = ['title', 'description', 'image', 'start_date', 'live_class_url']
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['title', 'course__title']
    fields = ['course', 'title', 'order']
    inlines = [VideoInline]

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'duration', 'order', 'created_at']
    list_filter = ['module__course', 'created_at']
    search_fields = ['title', 'module__title']
    fields = ['module', 'title', 'video_url', 'duration', 'order']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'course', 'user', 'enrolled_at']
    list_filter = ['course', 'enrolled_at']
    search_fields = ['name', 'email', 'course__title']
    readonly_fields = ['enrolled_at']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm
    list_display = ['user', 'created_at']
    search_fields = ['user__username', 'user__email']
    fields = ['user', 'photo', 'bio']

admin.site.site_header = 'Semicolons Course Management'
admin.site.site_title = 'Semicolons Admin'
admin.site.index_title = 'Course Management Dashboard'