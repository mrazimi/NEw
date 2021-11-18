# Generated by Django 3.2.9 on 2021-11-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0005_alter_patient_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='kind',
            field=models.IntegerField(blank=True, choices=[(0, 'جراحی 1'), (1, 'جراحی 2'), (2, 'جراحی 3'), (3, 'جراحی 4')], default=0, null=True, verbose_name='نوع جراحی'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='file_number',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='کد ملی/شناسه'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='description',
            field=models.TextField(max_length=200, verbose_name='توضیحات'),
        ),
    ]