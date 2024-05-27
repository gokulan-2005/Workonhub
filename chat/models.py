from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

# Create your models here.
class customer_details(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    
class ThreadManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs


class Thread(models.Model):
    first_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='thread_first_person')
    second_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='thread_second_person')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()
    class Meta:
        unique_together = ['first_person', 'second_person']

class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.CASCADE, related_name='chatmessage_thread')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    text = models.TextField()
    music = models.FileField(upload_to='uploads/', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    video = models.FileField(upload_to='uploads/', blank=True, null=True)
    camera_image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class User_info(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    e_mail = models.EmailField()
    Mobno = models.CharField(max_length=10)
    birth_date = models.DateField(default=timezone.now)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=50)
    message = models.TextField()