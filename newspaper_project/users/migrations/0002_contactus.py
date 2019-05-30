# Generated by Django 2.2.1 on 2019-05-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default=True, max_length=20)),
                ('lastname', models.CharField(default=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('phonenumber', models.IntegerField(max_length=13)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
