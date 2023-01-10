# SPDX-FileCopyrightText: Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.1.7 on 2021-03-03 07:14

from django.db import migrations


def fixup_enforced_checks(apps, schema_editor):
    Component = apps.get_model("trans", "Component")
    db_alias = schema_editor.connection.alias
    for c in Component.objects.using(db_alias).all():
        if c.enforced_checks == "":
            c.enforced_checks = []
            c.save(update_fields=["enforced_checks"])


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0122_auto_20210228_1846"),
    ]

    operations = [migrations.RunPython(fixup_enforced_checks, elidable=True)]
