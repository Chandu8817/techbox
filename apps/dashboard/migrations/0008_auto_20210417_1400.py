# Generated by Django 3.1.7 on 2021-04-17 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20210416_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.FileField(default='media/img/undraw_profile.svg', upload_to='media/img'),
        ),
        migrations.AlterField(
            model_name='toolsissue',
            name='borrowTime',
            field=models.DateTimeField(),
        ),
    ]
