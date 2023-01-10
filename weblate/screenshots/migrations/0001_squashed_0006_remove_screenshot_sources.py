# SPDX-FileCopyrightText: Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.5 on 2020-04-16 11:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import weblate.screenshots.fields


class Migration(migrations.Migration):

    replaces = [
        ("screenshots", "0001_squashed_0003_auto_20170215_1633"),
        ("screenshots", "0002_auto_20180826_0839"),
        ("screenshots", "0003_auto_20190516_1248"),
        ("screenshots", "0004_screenshot_units"),
        ("screenshots", "0005_source_strings"),
        ("screenshots", "0006_remove_screenshot_sources"),
    ]

    initial = True

    dependencies = [
        ("trans", "0046_source_strings"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Screenshot",
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
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="Screenshot name"),
                ),
                (
                    "image",
                    weblate.screenshots.fields.ScreenshotField(
                        help_text="Upload JPEG or PNG images up to 2000x2000 pixels.",
                        upload_to="screenshots/",
                        verbose_name="Image",
                    ),
                ),
                (
                    "component",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.Component",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "units",
                    models.ManyToManyField(
                        blank=True, related_name="screenshots", to="trans.Unit"
                    ),
                ),
            ],
            options={},
        ),
    ]
