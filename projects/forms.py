from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Projects

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

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profile_pic','bio']
        
class ProjectForm(forms.ModelForm):
    language=forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=languages
    )
    
    technologies=forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=technologies
    )
    
    class Meta:
        model=Projects
        fields=['project_title','project_about','project_description','screen_shot','technologies','language']