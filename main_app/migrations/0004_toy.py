# Generated by Django 4.2.7 on 2023-11-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_feeding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
    ]
