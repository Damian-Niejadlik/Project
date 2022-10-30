from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True, null=False, auto_created=True, verbose_name="id",)
    username = models.CharField(max_length=25, unique=True, verbose_name='username',)
