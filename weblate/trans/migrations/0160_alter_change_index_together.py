# SPDX-FileCopyrightText: Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.1.3 on 2022-11-13 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lang", "0017_alter_plural_type"),
        ("trans", "0159_alter_change_index_together_alter_change_timestamp_and_more"),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name="change",
            index_together={
                ("timestamp", "project", "component", "language", "action"),
                ("action", "translation", "timestamp"),
            },
        ),
    ]
