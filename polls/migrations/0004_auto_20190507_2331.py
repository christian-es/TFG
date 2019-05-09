# Generated by Django 2.2 on 2019-05-07 21:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(on_delete='models.CASCADE', related_name='teacher_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
