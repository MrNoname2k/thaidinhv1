from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=True)
    phone_regex = RegexValidator(regex=r'/(84|0[3|5|7|8|9])+([0-9]{8})\b/g')
    phone = models.CharField(validators=[phone_regex],max_length=11,null=False,blank=False)
    address = models.CharField(max_length=300,null=False,blank=False)
    gender = models.BooleanField(default=False)

def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user = instance)

post_save.connect(create_user_profile, sender=User)



    
