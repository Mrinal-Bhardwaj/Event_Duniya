from django.db import models
from PIL import Image


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    Name_of_event = models.CharField(max_length=50, default='')
    pic_or_logo = models.ImageField(null=True, blank=True, upload_to="image")
    location = models.CharField(max_length=100, default='')
    duration = models.CharField(max_length=100, default='')
    time = models.CharField(max_length=20, default='')
    venue = models.CharField(max_length=100, default='')
    industry = models.CharField(max_length=20, default='')
    organizer = models.CharField(max_length=50, default='')
    link_to_register = models.CharField(max_length=200, default='')
    type_of_event = models.CharField(max_length=50, default='')
    post_or_not = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.pic_or_logo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.pic_or_logo.path)

    def __str__(self):
        return self.Name_of_event


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=100, default='')
    phone = models.CharField(max_length=20, default='')
    query = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.name


class About(models.Model):
    About_Id = models.AutoField(primary_key=True, default='')
    own_pic = models.ImageField()
    about_urslf = models.CharField(max_length=500)

    def __str__(self):
        return self.about_urslf
