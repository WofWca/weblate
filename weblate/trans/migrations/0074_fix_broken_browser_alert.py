# Generated by Django 3.0.5 on 2020-04-12 05:09

from django.db import migrations


def migrate_alerts(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Alert = apps.get_model("trans", "Alert")
    for alert in Alert.objects.using(db_alias).filter(name="BrokenBrowserURL"):
        if "links" in alert.details:
            alert.details = {
                "link": alert.details["links"][0],
                "error": "",
            }
            alert.save(update_fields=["details"])


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0073_auto_20200403_1329"),
    ]

    operations = [
        migrations.RunPython(migrate_alerts, migrations.RunPython.noop, elidable=True)
    ]
