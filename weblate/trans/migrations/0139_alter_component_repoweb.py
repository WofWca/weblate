# SPDX-FileCopyrightText: Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.2.4 on 2021-08-19 07:30

from django.db import migrations, models

import weblate.utils.render


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0138_alter_component_report_source_bugs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="component",
            name="repoweb",
            field=models.URLField(
                blank=True,
                help_text="Link to repository browser, use {{branch}} for branch, {{filename}} and {{line}} as filename and line placeholders. You might want to strip leading directory by using {{filename|parentdir}}.",
                validators=[weblate.utils.render.validate_repoweb],
                verbose_name="Repository browser",
            ),
        ),
    ]
