# Generated by Django 4.1.3 on 2022-11-08 01:38

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
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('link', models.CharField(max_length=100)),
                ('logged', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('A', 'Applied'), ('I', 'Interviewed'), ('R', 'Rejected')], default='A', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.application')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.application')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.application')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.company')),
            ],
        ),
    ]
