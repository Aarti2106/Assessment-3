# Generated by Django 4.1.7 on 2023-03-14 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='account_name',
            new_name='cpassword',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='re_enterpassword',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='usertype',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='', upload_to='upload_new_photo/'),
            preserve_default=False,
        ),
    ]
