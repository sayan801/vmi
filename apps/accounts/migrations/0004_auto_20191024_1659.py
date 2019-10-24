# Generated by Django 2.2.4 on 2019-10-24 16:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191016_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(blank=True, help_text='Employees or contractors acting on behalf of the Organization.', related_name='org_staff', to=settings.AUTH_USER_MODEL, verbose_name='Organizational Agents'),
        ),
    ]
