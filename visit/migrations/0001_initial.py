# Generated by Django 3.2.9 on 2021-11-15 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('file_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=120, verbose_name='نام کامل')),
                ('age', models.IntegerField(null=True, verbose_name='تاریخ تولد')),
                ('phone', models.CharField(max_length=11, null=True, verbose_name='تلفن')),
            ],
            options={
                'verbose_name': 'بیمار',
                'verbose_name_plural': 'بیمار',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='زمان مراجعه')),
                ('description', models.TextField(max_length=250, verbose_name='توضیحات')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.profile', verbose_name='دکتر')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='visit.patient', verbose_name='بیمار')),
            ],
            options={
                'verbose_name': 'ویزیت',
                'verbose_name_plural': 'ویزیت',
            },
        ),
    ]
