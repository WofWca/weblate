# SPDX-FileCopyrightText: Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.7 on 2020-09-07 11:39

from django.db import migrations


def migrate_source_language(apps, schema_editor):
    Project = apps.get_model("trans", "Project")
    db_alias = schema_editor.connection.alias
    for project in Project.objects.using(db_alias).iterator():
        project.component_set.update(source_language=project.source_language)


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0097_component_source_language"),
    ]

    operations = [migrations.RunPython(migrate_source_language, elidable=True)]
