# Generated by Django 3.2.7 on 2021-09-30 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NotesAdda', '0002_alter_uploadfiles_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='myFile',
            field=models.FileField(upload_to='pdfs/'),
        ),
        migrations.AlterField(
            model_name='uploadfiles',
            name='semName',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='uploadfiles',
            name='year',
            field=models.PositiveSmallIntegerField(),
        ),
    ]