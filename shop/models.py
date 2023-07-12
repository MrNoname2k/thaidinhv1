from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save

CATEGORY_CHOICES = (
    ('VT', 'Vòng Tay'),
    ('DC', 'Dây Chuyền'),
    ('TD', 'Trầm Đốt'),
    ('NT','Nụ Trầm')
)

STATUS_CHOICES = (
    ('CH', 'Còn Hàng'),
    ('HH', 'Hết Hàng'),
    ('YC', 'Yêu Cầu')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    description = models.TextField()
    image = models.ImageField(upload_to='item/')

    def __str__(self):
        return self.title