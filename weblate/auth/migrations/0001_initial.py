# SPDX-FileCopyrightText: Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 1.11.12 on 2018-05-07 13:03

import django.utils.timezone
from django.db import migrations, models

import weblate.auth.models
import weblate.utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Username may only contain letters, numbers or the following characters: @ . + - _",
                        max_length=150,
                        unique=True,
                        validators=[weblate.utils.validators.validate_username],
                        verbose_name="Username",
                    ),
                ),
                (
                    "full_name",
                    models.CharField(
                        max_length=150,
                        validators=[weblate.utils.validators.validate_fullname],
                        verbose_name="Full name",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        validators=[weblate.utils.validators.validate_email],
                        verbose_name="Email",
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="User has all possible permissions.",
                        verbose_name="Superuser status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Mark user as inactive instead of removing.",
                        verbose_name="Active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Date joined"
                    ),
                ),
            ],
            options={"abstract": False},
            managers=[("objects", weblate.auth.models.UserManager())],
        )
    ]
