from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_google_maps.fields import AddressField, GeoLocationField
from pyuploadcare.dj.models import ImageField

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
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)

    @classmethod
    def status_by_user(cls, username):
        status = Status.objects.filter(user__username = username)
        return status
    
    @classmethod
    def status_by_hood(cls, hood_id):
        status = Status.objects.filter(hood__pk = hood_id)
        return status
    
    def __str__(self):
        return self.user.username

class Business(models.Model):
    business_name = models.CharField(max_length=100)
    business_email = models.EmailField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)
    business_hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.business_name

class Bio(models.Model):
    nickname = models.CharField(max_length=50, blank=True)
    user_bio = models.TextField(blank=True)
    # user_pic = models.ImageField(upload_to = 'p/', default='image')
    user_upic = ImageField(blank=True, manual_crop='800x800')
    user_hood = models.ForeignKey(Hood, on_delete=models.CASCADE, blank=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    @classmethod
    def get_bio_by_user(cls, username):
        profile = Bio.objects.get(user__username = username)
        return profile

    def __str__(self):
        return self.user.username

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Bio.objects.create(user=instance)
        except Exception as error:
            # print(error)
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
