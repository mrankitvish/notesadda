# Generated by Django 3.2.9 on 2021-11-10 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='files',
            name='pdf',
            field=models.FileField(upload_to='pdfs/'),
        ),
    ]
