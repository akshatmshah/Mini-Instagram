from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)

    class Meta:
        app_label = "insta"

    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True, unique=False)
    text = models.TextField(default="", blank=True, max_length=100, null=True)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    class Meta:
        app_label = "insta"

    def __str__(self):
        return self.text
