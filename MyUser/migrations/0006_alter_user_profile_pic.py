# Generated by Django 5.1.3 on 2024-11-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyUser', '0005_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='ids/'),
        ),
    ]