# SPDX-FileCopyrightText: Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.6 on 2020-05-19 14:36

from django.db import migrations

import weblate.trans.fields


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0078_auto_20200515_0729"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Shaping",
            new_name="Variant",
        ),
        migrations.AlterModelOptions(
            name="variant",
            options={
                "verbose_name": "variant definition",
                "verbose_name_plural": "variant definitions",
            },
        ),
        migrations.RenameField(
            model_name="variant",
            old_name="shaping_regex",
            new_name="variant_regex",
        ),
        migrations.AlterUniqueTogether(
            name="variant",
            unique_together={("key", "component", "variant_regex")},
        ),
        migrations.RenameField(
            model_name="unit",
            old_name="shaping",
            new_name="variant",
        ),
        migrations.RenameField(
            model_name="component",
            old_name="shaping_regex",
            new_name="variant_regex",
        ),
        migrations.AlterField(
            model_name="component",
            name="variant_regex",
            field=weblate.trans.fields.RegexField(
                blank=True,
                default="",
                help_text="Regular expression used to determine variants of a string.",
                max_length=190,
                validators=[weblate.utils.validators.validate_re_nonempty],
                verbose_name="Variants regular expression",
            ),
        ),
    ]
