from os import listdir, path
from cloudinary import api
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.core.exceptions import ValidationError
from django.db.models.query_utils import Q
from CS490.settings import MEDIA_DIR
from app.validators import MinAgeValidator
from cloudinary.models import CloudinaryField

import random
# Create your models here.


def random_img():
    default_img = MEDIA_DIR.joinpath('default')
    rand = random.choice(listdir(default_img))
    print(path.join(default_img, rand))
    return path.join('default', rand)


class Follower(models.Model):
    follower = models.ForeignKey(
        User, on_delete=CASCADE, related_name='following')
    following = models.ForeignKey(
        User, on_delete=CASCADE, related_name='followers')

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
    # additional

    date_of_birth = models.DateField(validators=[MinAgeValidator(18)])
    profile_pic = CloudinaryField(
        allowed_formats=['jpg', 'png', 'gif'], folder="profile_pics/", default=random_img)
    user_bio = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

class UserAnnoucement(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    announcement = models.TextField(max_length=280)
    image = CloudinaryField(
        allowed_formats=['jpg', 'png'], folder="user_files/", blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.username + "-->" + self.announcement


class UserComment(models.Model):
    post = models.ForeignKey(UserAnnoucement, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    comment = models.TextField(max_length=280)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.username + "  --Commented on--> " + self.post.announcement

class ThreadManager(models.Manager):
    def by_user(self, user):
        qlookup = Q(first=user) | Q(second=user)
        qlookup2 = Q(first=user) & Q(second=user)
        qs = self.get_queryset().filter(qlookup).exclude(qlookup2).distinct()
        return qs

    def get_or_new(self, user, other_username): # get_or_create
        username = user.username
        if username == other_username:
            return None
        qlookup1 = Q(first__username=username) & Q(second__username=other_username)
        qlookup2 = Q(first__username=other_username) & Q(second__username=username)
        qs = self.get_queryset().filter(qlookup1 | qlookup2).distinct()
        if qs.count() == 1:
            return qs.first(), False
        elif qs.count() > 1:
            return qs.order_by('timestamp').first(), False
        else:
            Klass = user.__class__
            user2 = Klass.objects.get(username=other_username)
            if user != user2:
                obj = self.model(
                        first=user, 
                        second=user2
                    )
                obj.save()
                return obj, True
            return None, False


class Thread(models.Model):
    first        = models.ForeignKey(User, on_delete=CASCADE, related_name='chat_thread_first')
    second       = models.ForeignKey(User, on_delete=CASCADE, related_name='chat_thread_second')
    updated      = models.DateTimeField(auto_now=True)
    timestamp    = models.DateTimeField(auto_now_add=True)
    
    objects      = ThreadManager()

    @property
    def room_group_name(self):
        return f'chat_{self.id}'

    def clean(self):
        super().clean()
        if self.first == self.second:
            raise ValidationError('You can not message yourself')

    def __str__(self):
        return u'%s <- nessage thread -> %s' % (self.first, self.second)


class ChatMessage(models.Model):
    thread      = models.ForeignKey(Thread, null=True, blank=True, on_delete=SET_NULL)
    user        = models.ForeignKey(User, verbose_name='sender', on_delete=CASCADE)
    message     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)
