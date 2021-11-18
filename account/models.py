from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class profile(models.Model):
    class Meta:
        verbose_name = 'ساخت حساب دکتر'
        verbose_name_plural = 'ساخت حساب دکتر'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='حساب کاربری', null=True)
    fullname = models.CharField('نام کامل', max_length=120, default='')
    age = models.IntegerField('سن', null=True)
    city = models.CharField('شهر', max_length=50, null=True)
    phone = models.CharField('تلفن', max_length=12, null=True)

    Secretary, Doctor, AdminSystem = 0, 1, 2
    role_list = [(Secretary, 'منشی (سطح 0)'), (Doctor, 'دکتر (سطح 1)'), (AdminSystem, 'ادمین سیستم (سطح 3)')]
    role = models.IntegerField(choices=role_list, null=True, default=0, blank=True)

    General, Specialist, SuperSpecialist = 0, 1, 2
    deg = [(General, 'عمومی'), (Specialist, 'تخصص'), (SuperSpecialist, 'فوق تخصص')]
    degree = models.IntegerField('درجه تحصیلی', choices=deg, null=True, blank=True)

    title = models.CharField('عنوان دکتر', null=True, max_length=50)
    address = models.TextField('آدرس', null=True)

    def __str__(self):
        return '%s - %s - (%s)' % (self.user.username, self.fullname, self.title)
