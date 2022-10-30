from django.db import models


class Image(models.Model):
    image_name = models.CharField(max_length=40, unique=True)
    comment = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("register.Users", on_delete=models.CASCADE)
    # directory = f"{str(user)}/images"
    image = models.ImageField(upload_to='test/')
