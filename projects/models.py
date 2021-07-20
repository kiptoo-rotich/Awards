from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
import datetime as dt

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(blank=True,max_length=400)
    profile_pic = CloudinaryField('image',default='Image')
    country=models.CharField(blank=True,max_length=20)
    company=models.CharField(blank=True,max_length=20,null=True)
    portfolio_link=models.CharField(blank=True,max_length=50,null=True)
    phone_number=models.CharField(max_length=13)

    def __str__(self):
        return self.bio
    
@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
class Projects(models.Model):
    project_title = models.CharField(max_length=30)
    project_about = models.CharField(max_length=30)
    project_description = models.TextField()
    screen_shot = CloudinaryField('image' ,default='Image')
    technologies=models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering=['-posted_on']

    def __str__(self):
        return self.project_title
    
    @classmethod
    def search(cls,search_term):
        projects=cls.objects.filter(project_title__icontains=search_term)
        return projects

class Review(models.Model):
    reviews = models.TextField(max_length=200)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering=['-posted_on']