from django.db import models


class Image(models.Model):
    image_name = models.CharField(max_length=40, unique=True, )
    image_id = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("register.User", on_delete=models.CASCADE)
    directory = f"{str(user)}/images"
    image = models.ImageField(upload_to=directory)
