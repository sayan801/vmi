# Generated by Django 2.1.2 on 2018-12-31 15:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fido', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attestedcredentialdata',
            old_name='credential_id',
            new_name='_credential_id',
        ),
        migrations.RenameField(
            model_name='attestedcredentialdata',
            old_name='public_key',
            new_name='_public_key',
        ),
        migrations.AddField(
            model_name='attestedcredentialdata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attestedcredentialdata',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='attestedcredentialdata',
            name='_credential_id',
            field=models.BinaryField(db_column='credential_id'),
        ),
        migrations.AlterField(
            model_name='attestedcredentialdata',
            name='_public_key',
            field=models.BinaryField(db_column='public_key'),
        ),
    ]