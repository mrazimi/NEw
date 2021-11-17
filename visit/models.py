from django.db import models
from jalali_date import date2jalali, datetime2jalali


# Create your models here.
class Patient(models.Model):
    class Meta:
        verbose_name = 'بیمار'
        verbose_name_plural = 'بیمار'

    file_number = models.CharField(primary_key=True, max_length=10)
    fullname = models.CharField('نام کامل', max_length=120)
    age = models.DateTimeField('تاریخ تولد', null=True)
    doctor = models.ForeignKey('account.profile', on_delete=models.DO_NOTHING, verbose_name='دکتر')
    phone = models.CharField('تلفن', max_length=11, null=True)

    def __str__(self):
        return '%s (%s)' % (self.fullname, self.file_number)


class Visit(models.Model):
    class Meta:
        verbose_name = 'ویزیت'
        verbose_name_plural = 'ویزیت'

    patient = models.ForeignKey('Patient', on_delete=models.DO_NOTHING, verbose_name='بیمار')
    doctor = models.ForeignKey('account.profile', on_delete=models.DO_NOTHING, verbose_name='دکتر')
    datetime = models.DateTimeField('زمان مراجعه', auto_now_add=True)
    description = models.TextField('توضیحات', max_length=250)

    def to_jalali(self):
        return datetime2jalali(self.datetime)

    def __str__(self):
        return '(بیمار:%s) - (تاریخ:%s)' % (self.patient, self.datetime)
