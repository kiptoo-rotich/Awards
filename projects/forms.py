from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Projects,Review

languages=[
    ('django', 'django'),
    ('Flask','Flask'),
    ('Angular', 'Angular'),
    ('Javascript', 'Javascript'),
    ('Python', 'Python'),
    ('C#', 'C#'),
    ('Java','Java'),
    ('C', 'C'),
    ('Swift','Swift'),
]

technologies=[
    ('django', 'django'),
    ('Flask','Flask'),
    ('Angular', 'Angular'),
    ('Javascript', 'Javascript'),
    ('Python', 'Python'),
    ('C#', 'C#'),
    ('Java','Java'),
    ('C', 'C'),
    ('Swift','Swift'),
    ('git','git'),
    ('postgresql','postgresql'),
    ('bootstrap','bootstrap'),

]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profile_pic','bio','company','portfolio_link','phone_number']
        
class ProjectForm(forms.ModelForm):
 
    class Meta:
        model=Projects
        fields='__all__'
   
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['reviews']
