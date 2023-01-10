# SPDX-FileCopyrightText: Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.1.1 on 2020-10-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0104_update_source_unit_source"),
    ]

    operations = [
        migrations.AlterField(
            model_name="translation",
            name="language_code",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
    ]
