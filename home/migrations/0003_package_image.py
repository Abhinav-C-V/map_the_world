# Generated by Django 4.2.7 on 2023-12-02 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_package_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
