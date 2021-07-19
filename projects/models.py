from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True,max_length=400)
    profile_pic = CloudinaryField('image',default='Image')
    country=models.TextField(blank=True,max_length=20)

    def __str__(self):
        return self.user__username
    
@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
class Projects(models.Model):
    project_title = models.CharField(max_length=30)
    project_about = models.CharField(max_length=30)
    project_description = models.CharField(max_length=2000)
    screen_shot = CloudinaryField('image' ,default='Image')
    technologies=models.CharField(max_length=20)

    def __str__(self):
        return self.project_title
    
    @classmethod
    def search(cls,search_term):
        projects=cls.objects.filter(project_title__icontains=search_term)
        return projects

class Review(models.Model):
    reviews = models.TextField(max_length=200)
    project_id = models.ForeignKey('Projects', blank=True,on_delete=models.CASCADE)
    