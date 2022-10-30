from django.db import models


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True, blank=True, auto_created=True, verbose_name="id",)
    username = models.CharField(max_length=25, unique=True, verbose_name='username',)
