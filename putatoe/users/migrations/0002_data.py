# Generated by Django 3.2.15 on 2022-11-03 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('var1', models.CharField(blank=True, max_length=255, verbose_name='Editable Variable 1')),
            ],
        ),
    ]
