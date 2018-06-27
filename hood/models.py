from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_google_maps.fields import AddressField, GeoLocationField

# Create your models here.
class Hood(models.Model):
    name = models.CharField(max_length=150)
    location = GeoLocationField(blank=True)
    address = AddressField(max_length=100)
    
    def __str__(self):
        return self.address

class Status(models.Model):
    status_content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Business(models.Model):
    business_name = models.CharField(max_length=100)
    business_email = models.EmailField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)
    business_hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.business_name

class Bio(models.Model):
    nickname = models.CharField(max_length=50)
    user_bio = models.TextField()
    user_pic = models.ImageField(upload_to = 'p/', default='image')
    user_hood = models.ForeignKey(Hood, on_delete=models.CASCADE, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.nickname

def post_save_user_model_receiver(sender, instance,created,*args,**kwargs):
    if created:
        try:
            Bio.objects.create(user=instance)
        except:
            pass
post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
