# SPDX-FileCopyrightText: Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.6 on 2020-06-09 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0085_change_glossary_term"),
        ("glossary", "0002_migrate_dictionary"),
    ]

    operations = [
        migrations.RemoveField(model_name="change", name="dictionary"),
        migrations.DeleteModel(name="Dictionary"),
    ]
