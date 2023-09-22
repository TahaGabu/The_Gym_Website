# Generated by Django 4.2.4 on 2023-09-18 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymApp', '0010_alter_gymplans_options_gym_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookSlots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymApp.gym')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymApp.trainer')),
            ],
        ),
    ]
