# Generated by Django 4.0.10 on 2024-07-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_alter_catechumene_categorie_alter_catechumene_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='catechumene',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='catechumene_photos/'),
        ),
    ]
