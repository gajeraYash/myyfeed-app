from app.validators import MinAgeValidator
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    admin = models.BooleanField(default=False)
    #additional
    date_of_birth = models.DateField(validators=[MinAgeValidator(18)])
    profile_pic = models.ImageField(upload_to="profile_pics",blank=True)
    user_bio = models.CharField(max_length=256,blank=True)
    user_location = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username

class UserAnnoucements(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    announcement = models.TextField(max_length=512)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.username + "\n" + self.announcement