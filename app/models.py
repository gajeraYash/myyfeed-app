from django.core.exceptions import ValidationError
from CS490.settings import MEDIA_DIR
from app.validators import MinAgeValidator
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from os import listdir,path
import random
# Create your models here.
def random_img():
    default_img=MEDIA_DIR.joinpath('default')
    rand = random.choice(listdir(default_img))
    print(path.join(default_img, rand))
    return path.join('default', rand)

class Follower(models.Model):
    follower = models.ForeignKey(User,on_delete=CASCADE, related_name='following')
    following = models.ForeignKey(User,on_delete=CASCADE, related_name='followers')
    
    class Meta:
        unique_together = ('follower', 'following')

    def clean(self):
        super().clean()
        if self.follower == self.following:
            raise ValidationError('You can not follow yourself')


    def __str__(self):
        return u'%s ->follows-> %s' % (self.follower, self.following)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    admin = models.BooleanField(default=False)
    #additional

    date_of_birth = models.DateField(validators=[MinAgeValidator(18)])
    profile_pic = models.ImageField(upload_to="profile_pics", default=random_img)
    user_bio = models.CharField(max_length=256,blank=True)
    user_location = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in UserProfile._meta.fields]

class UserAnnoucement(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    announcement = models.TextField(max_length=280)
    image = models.ImageField(upload_to="user_files", blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.username + "---" + self.announcement

    def get_queryset(self):
        print("Get Field Called")
        return UserAnnoucement.objects.all()
