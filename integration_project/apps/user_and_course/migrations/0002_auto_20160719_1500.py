# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_registration', '0003_auto_20160719_1500'),
        ('user_and_course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users_in_courses',
            name='course_title',
        ),
        migrations.RemoveField(
            model_name='users_in_courses',
            name='num_users',
        ),
        migrations.AddField(
            model_name='users_in_courses',
            name='User_in_login',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login_and_registration.Users'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users_in_courses',
            name='User_in_Course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.Course'),
        ),
    ]
