# Generated by Django 2.2 on 2019-05-06 21:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0002_auto_20190424_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre del profesor', max_length=200)),
                ('last_name', models.CharField(help_text='Apellido del profesor', max_length=200)),
                ('user', models.OneToOneField(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]