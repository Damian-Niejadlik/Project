from django.db import models


class Image(models.Model):
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("user_app.Users", on_delete=models.CASCADE)
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/')
