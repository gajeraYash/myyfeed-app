from app.validators import MinAgeValidator
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Follower(models.Model):
    follower = models.ForeignKey(User,on_delete=CASCADE, related_name='following')
    following = models.ForeignKey(User,on_delete=CASCADE, related_name='followers')
    
    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return self.follower + '->follow->' + self.following

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
    announcement = models.TextField(max_length=280)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.username + "---" + self.announcement