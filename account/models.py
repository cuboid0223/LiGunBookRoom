from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings # 使用者頭像
imgUser = settings.AUTH_USER_MODEL  # 使用者頭像
# Create your models here.

class User(AbstractUser):
    fullName = models.CharField(max_length=128)
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    

    def __str__(self):
        return self.fullName+'(' + self.username + ')'



    
