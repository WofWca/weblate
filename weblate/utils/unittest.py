# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import tempfile

from django.test.utils import override_settings

from weblate.utils.files import remove_tree


# Lowercase name to be consistent with Django
# pylint: disable=invalid-name
class tempdir_setting(override_settings):  # noqa
    def __init__(self, setting):
        kwargs = {setting: None}
        super().__init__(**kwargs)
        self._tempdir = None
        self._setting = setting

    def enable(self):
        self._tempdir = tempfile.mkdtemp()
        self.options[self._setting] = self._tempdir
        super().enable()

    def disable(self):
        super().disable()
        if self._tempdir is not None:
            remove_tree(self._tempdir)
            self._tempdir = None
