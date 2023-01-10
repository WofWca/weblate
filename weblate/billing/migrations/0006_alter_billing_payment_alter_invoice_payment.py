# SPDX-FileCopyrightText: Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.1 on 2022-09-15 10:59

from django.db import migrations

import weblate.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("billing", "0005_auto_20210512_1955"),
    ]

    operations = [
        migrations.AlterField(
            model_name="billing",
            name="payment",
            field=weblate.utils.fields.JSONField(default=dict, editable=False),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="payment",
            field=weblate.utils.fields.JSONField(default=dict, editable=False),
        ),
    ]
