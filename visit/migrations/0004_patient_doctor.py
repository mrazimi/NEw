# Generated by Django 3.2.9 on 2021-11-17 15:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_role'),
        ('visit', '0003_alter_patient_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.profile', verbose_name='دکتر'),
            preserve_default=False,
        ),
    ]
