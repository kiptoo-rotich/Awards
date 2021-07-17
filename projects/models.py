from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True,max_length=400)
    profile_pic=models.ImageField()
    country=models.TextField(blank=True,max_length=20)

@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
class Projects(models.Model):
    project_title = models.CharField(max_length=30)
    project_about = models.CharField(max_length=30)
    project_description = models.CharField(max_length=2000)
    screen_shot=models.ImageField()
    technologies=models.CharField(max_length=20)
    