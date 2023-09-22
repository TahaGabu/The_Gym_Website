# Generated by Django 4.2.4 on 2023-09-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymApp', '0003_gymadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.DateField()),
                ('height', models.IntegerField(max_length=100)),
                ('weight', models.IntegerField(max_length=100)),
                ('address', models.TextField()),
                ('number', models.IntegerField()),
            ],
        ),
    ]