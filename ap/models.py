from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key = True)
    title = models.TextField(max_length = 20, default="title")
    landing_page_image = models.ImageField(upload_to = 'images/')
    description = models.TextField()

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

@classmethod
def search_projects(cls , search_term):
    projects = cls.objects.filter( first_name__icontains = search_term )
    return projects

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_photo = models.ImageField(upload_to='profile/')
    bio = models.CharField(max_length=200)
    projects = models.ForeignKey(Projects, null=True)
    user_contact_info=models.IntegerField(default=0)

