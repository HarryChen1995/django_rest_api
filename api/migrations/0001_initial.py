# Generated by Django 3.2.7 on 2021-09-11 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('content', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
