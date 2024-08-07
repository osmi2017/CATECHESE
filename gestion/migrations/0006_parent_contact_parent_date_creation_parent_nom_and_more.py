# Generated by Django 4.0.10 on 2024-07-27 12:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_animateur_contact_animateur_date_creation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='contact',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parent',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parent',
            name='nom',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parent',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='parent_photos/'),
        ),
        migrations.AddField(
            model_name='parent',
            name='prenom',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
