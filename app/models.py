from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    #additional
    date_of_birth = models.DateField()
    profile_pic = models.ImageField(upload_to="profile_pics",blank=True)
    user_bio = models.CharField(max_length=256,blank=True)
    user_location = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username