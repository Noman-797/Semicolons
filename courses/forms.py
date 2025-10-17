from django import forms
from .models import UserProfile, Course
from cloudinary.forms import CloudinaryFileField

class UserProfileForm(forms.ModelForm):
    photo = CloudinaryFileField(
        options={
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'profile_photos'
        },
        required=False
    )
    
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'class': 'block w-full shadow-sm sm:text-sm border-border-light dark:border-border-dark rounded-lg bg-background-light dark:bg-background-dark focus:ring-primary focus:border-primary',
            'placeholder': 'Tell us about yourself...'
        }),
        required=False
    )
    
    class Meta:
        model = UserProfile
        fields = ['photo', 'bio']

class CourseForm(forms.ModelForm):
    image = CloudinaryFileField(
        options={
            'crop': 'fill',
            'width': 400,
            'height': 300,
            'folder': 'course_images'
        },
        required=False
    )
    
    class Meta:
        model = Course
        fields = ['title', 'description', 'image', 'start_date', 'live_class_url']