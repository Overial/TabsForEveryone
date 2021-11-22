# Generated by Django 3.2.8 on 2021-11-22 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('band', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=100)),
                ('instrument', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('tab_image', models.ImageField(upload_to='images/')),
                ('audio_file', models.FileField(upload_to='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
