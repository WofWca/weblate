# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from datetime import date

from celery.schedules import crontab

from weblate.utils.celery import app
from weblate.utils.lock import WeblateLockTimeout
from weblate.wladmin.models import BackupService, SupportStatus


@app.task(trail=False)
def support_status_update():
    support = SupportStatus.objects.get_current()
    if support.secret:
        support.refresh()
        support.save()


@app.task(trail=False)
def backup():
    for service in BackupService.objects.filter(enabled=True):
        backup_service.delay(service.pk)


@app.task(trail=False, autoretry_for=(WeblateLockTimeout,))
def backup_service(pk):
    service = BackupService.objects.get(pk=pk)
    service.ensure_init()
    service.backup()
    service.prune()
    today = date.today()
    if today.weekday() == 3:
        service.cleanup()


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        24 * 3600, support_status_update.s(), name="support-status-update"
    )
    sender.add_periodic_task(crontab(hour=2, minute=0), backup.s(), name="backup")
