# SPDX-FileCopyrightText: Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.5 on 2020-04-16 11:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import weblate.utils.fields
import weblate.utils.render


class Migration(migrations.Migration):

    replaces = [
        ("accounts", "0001_squashed_0037_auto_20180416_1406"),
        ("accounts", "0002_profile_uploaded"),
        ("accounts", "0003_profile_translate_mode"),
        ("accounts", "0004_create_profile"),
        ("accounts", "0005_auto_20190331_2126"),
        ("accounts", "0006_subscriptions"),
        ("accounts", "0007_auto_20190411_0807"),
        ("accounts", "0008_auto_20190426_0941"),
        ("accounts", "0009_profile_zen_mode"),
        ("accounts", "0010_auto_20190516_1153"),
        ("accounts", "0011_auto_20190721_1810"),
        ("accounts", "0012_auto_20190805_1248"),
        ("accounts", "0013_auto_20190916_1203"),
        ("accounts", "0014_auto_20190922_1947"),
        ("accounts", "0015_auto_20190922_1948"),
        ("accounts", "0016_auto_20191115_2020"),
        ("accounts", "0017_auto_20200318_1014"),
        ("accounts", "0018_announcement_rename"),
        ("accounts", "0019_auto_20200403_2004"),
    ]

    initial = True

    dependencies = [
        ("trans", "0024_resolve_auto_format"),
        ("lang", "0001_squashed_0011_auto_20180215_1158"),
        ("trans", "0001_squashed_0143_auto_20180609_1655"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("social_django", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                    "language",
                    models.CharField(
                        blank=True,
                        choices=settings.LANGUAGES,
                        max_length=10,
                        verbose_name="Interface Language",
                    ),
                ),
                ("suggested", models.IntegerField(db_index=True, default=0)),
                ("translated", models.IntegerField(db_index=True, default=0)),
                (
                    "languages",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Choose the languages you can translate to. These will be offered to you on the dashboard for easier access to your chosen translations.",
                        to="lang.Language",
                        verbose_name="Translated languages",
                    ),
                ),
                (
                    "secondary_languages",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Choose languages you can understand, strings in those languages will be shown in addition to the source string.",
                        related_name="secondary_profile_set",
                        to="lang.Language",
                        verbose_name="Secondary languages",
                    ),
                ),
                (
                    "watched",
                    models.ManyToManyField(
                        blank=True,
                        help_text="You can receive notifications for watched projects and they are shown on the dashboard by default.",
                        to="trans.Project",
                        verbose_name="Watched projects",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "hide_completed",
                    models.BooleanField(
                        default=False,
                        verbose_name="Hide completed translations on the dashboard",
                    ),
                ),
                (
                    "secondary_in_zen",
                    models.BooleanField(
                        default=True,
                        verbose_name="Show secondary translations in the Zen mode",
                    ),
                ),
                (
                    "hide_source_secondary",
                    models.BooleanField(
                        default=False,
                        verbose_name="Hide source if a secondary translation exists",
                    ),
                ),
                (
                    "dashboard_component_list",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.ComponentList",
                        verbose_name="Default component list",
                    ),
                ),
                (
                    "dashboard_view",
                    models.IntegerField(
                        choices=[
                            (1, "Watched translations"),
                            (6, "Component lists"),
                            (4, "Component list"),
                            (5, "Suggested translations"),
                        ],
                        default=1,
                        verbose_name="Default dashboard view",
                    ),
                ),
                (
                    "editor_link",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Enter a custom URL to be used as link to the source code. You can use {{branch}} for branch, {{filename}} and {{line}} as filename and line placeholders.",
                        max_length=200,
                        validators=[weblate.utils.render.validate_editor],
                        verbose_name="Editor link",
                    ),
                ),
                (
                    "special_chars",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="You can specify additional special visual keyboard characters to be shown while translating. It can be useful for characters you use frequently, but are hard to type on your keyboard.",
                        max_length=30,
                        verbose_name="Special characters",
                    ),
                ),
                ("uploaded", models.IntegerField(db_index=True, default=0)),
                (
                    "translate_mode",
                    models.IntegerField(
                        choices=[(0, "Full editor"), (1, "Zen mode")],
                        default=0,
                        verbose_name="Translation editor mode",
                    ),
                ),
                (
                    "zen_mode",
                    models.IntegerField(
                        choices=[(0, "Top to bottom"), (1, "Side by side")],
                        default=0,
                        verbose_name="Zen editor mode",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VerifiedEmail",
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
                ("email", models.EmailField(max_length=254)),
                (
                    "social",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="social_django.UserSocialAuth",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subscription",
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
                    "notification",
                    models.CharField(
                        choices=[
                            ("MergeFailureNotification", "Repository failure"),
                            ("RepositoryNotification", "Repository operation"),
                            ("ParseErrorNotification", "Parse error"),
                            ("NewStringNotificaton", "New string"),
                            ("NewContributorNotificaton", "New contributor"),
                            ("NewSuggestionNotificaton", "New suggestion"),
                            (
                                "LastAuthorCommentNotificaton",
                                "Comment on own translation",
                            ),
                            ("MentionCommentNotificaton", "Mentioned in comment"),
                            ("NewCommentNotificaton", "New comment"),
                            ("ChangedStringNotificaton", "Changed string"),
                            ("NewTranslationNotificaton", "New language"),
                            ("NewComponentNotificaton", "New translation component"),
                            ("NewAnnouncementNotificaton", "New announcement"),
                            ("NewAlertNotificaton", "New alert"),
                            ("PendingSuggestionsNotification", "Pending suggestions"),
                            ("ToDoStringsNotification", "Unfinished strings"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "scope",
                    models.IntegerField(
                        choices=[
                            (10, "Defaults"),
                            (20, "Admin"),
                            (30, "Project"),
                            (40, "Component"),
                        ]
                    ),
                ),
                (
                    "frequency",
                    models.IntegerField(
                        choices=[
                            (0, "Do not notify"),
                            (1, "Instant notification"),
                            (2, "Daily digest"),
                            (3, "Weekly digest"),
                            (4, "Monthly digest"),
                        ]
                    ),
                ),
                (
                    "component",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.Component",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.Project",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {
                    ("notification", "scope", "project", "component", "user")
                },
            },
        ),
        migrations.CreateModel(
            name="AuditLog",
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
                    "activity",
                    models.CharField(
                        choices=[
                            ("auth-connect", "auth-connect"),
                            ("auth-disconnect", "auth-disconnect"),
                            ("connect", "connect"),
                            ("email", "email"),
                            ("failed-auth", "failed-auth"),
                            ("full_name", "full_name"),
                            ("invited", "invited"),
                            ("locked", "locked"),
                            ("login", "login"),
                            ("login-new", "login-new"),
                            ("password", "password"),
                            ("register", "register"),
                            ("removed", "removed"),
                            ("reset", "reset"),
                            ("reset-request", "reset-request"),
                            ("tos", "tos"),
                            ("username", "username"),
                        ],
                        db_index=True,
                        max_length=20,
                    ),
                ),
                ("params", weblate.utils.fields.JSONField(default={})),
                ("address", models.GenericIPAddressField(null=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("user_agent", models.CharField(default="", max_length=200)),
            ],
            options={},
        ),
    ]
