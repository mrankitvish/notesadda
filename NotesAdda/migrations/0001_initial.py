# Generated by Django 3.2.7 on 2021-09-30 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('uni_coll', models.CharField(max_length=100)),
                ('branchName', models.CharField(max_length=100)),
                ('year', models.PositiveSmallIntegerField(max_length=1)),
                ('semName', models.PositiveSmallIntegerField(max_length=1)),
                ('date', models.DateField(auto_now=True)),
                ('myFile', models.FileField(upload_to='media/pdfs/')),
            ],
        ),
    ]