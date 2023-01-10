# SPDX-FileCopyrightText: Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.0.1 on 2022-01-26 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0146_alter_component_merge_style"),
        ("weblate_auth", "0019_alter_role_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="defining_project",
            field=models.ForeignKey(
                null=True,
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="defined_groups",
                to="trans.project",
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="name",
            field=models.CharField(max_length=150, verbose_name="Name"),
        ),
    ]
